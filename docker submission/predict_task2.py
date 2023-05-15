#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import SimpleITK as sitk
import os
import pandas as pd


input_image_dir = '/input_image/'
path_img = os.path.join(input_image_dir,'{}.nii.gz')
path_pred = '/output/mortality.csv'

result = []

list_case = [k.split('.')[0] for k in os.listdir(input_image_dir)]

for case in list_case:
    img = sitk.ReadImage(path_img.format(case))

    # ==========your logic here. Below we do airway volume counting and thresholding as an example==============
    img_numpy = sitk.GetArrayFromImage(img)
    pred = img_numpy.sum()/(img_numpy.shape[0]*img_numpy.shape[1]*img_numpy.shape[2])
    # ==========================================================================================================
    result.append(pred)
    # record the result

# save the result
result = pd.DataFrame(result,columns=['prediction'])
result['filename'] = list_case
result.to_csv(path_pred)
