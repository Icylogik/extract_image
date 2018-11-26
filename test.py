import pydicom as pdc
import numpy as np
import matplotlib.pyplot as plt
from extract_image import extract

dicom_file = '000000.dcm'

dicom_data = pdc.dcmread(dicom_file)
image, slice_location = extract(dicom_data)

plt.imshow(image,cmap=plt.cm.bone)
