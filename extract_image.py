import numpy as np

def get_LUT_value(data, window, level):
    """Apply the RGB Look-Up Table for the given
       data and window/level value."""
    try:
        window = window[0]
    except TypeError:
        pass
    try:
        level = level[0]
    except TypeError:
        pass
    
    return np.piecewise(data,
                        [data <= (level - 0.5 - (window - 1) / 2),
                         data > (level - 0.5 + (window - 1) / 2)],
                        [0, 255, lambda data: ((data - (level - 0.5)) /
                         (window - 1) + 0.5) * (255 - 0)])
                         
                         

def linear_transform(dicom_data):
    """Linearly rescale the dicom image using the 
       RescaleIntercept and RescaleSlope values 
       extracted from the given DICOM data."""
    im_int16 = dicom_data.pixel_array.astype(np.int16)
    im_int16[im_int16== -2000] = 0
    intercept = dicom_data.RescaleIntercept
    slope = dicom_data.RescaleSlope
    if slope != 1:
            im_int16 = slope * im_int16.astype(np.float64)
            im_int16 = im_int16.astype(np.int16)

    transformed_pic =   im_int16 + np.int16(intercept)
    
    return transformed_pic
    

                         
def extract(dicom_data):
    """Extract viewable image and the slice location 
       from the given dicom data."""
    pic = linear_transform(dicom_data)
    im_transformed = get_LUT_value(pic, dicom_data.WindowWidth,
                                dicom_data.WindowCenter)
    slice_loc = dicom_data.SliceLocation
    
    return im_transformed, slice_loc
                                
