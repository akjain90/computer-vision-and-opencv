# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:29:45 2019

@author: jain
"""

from pyimagesearch.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()

ap.add_argument("-i","--image", required = True, help = "path to the image to be scanned")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
ratio = image.shape[0]/500.0
orig = image.copy()
image = imutils.resize(image, height=500)
#cv2.imshow("original",orig)
#cv2.waitKey(0)
#cv2.imshow("resized", image)
#cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray,(5,5),0)
edged = cv2.Canny(gray,50,150)
cv2.imshow("Image", image)
cv2.imshow("Canny", edged)
cv2.waitKey(0)
