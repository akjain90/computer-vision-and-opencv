### referred: https://github.com/gkouros/intro-to-cv-ud810 ###
#imports
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os.path


if __name__ == '__main__':
    
    img1 = cv2.imread('./input/lena.jpg', cv2.IMREAD_COLOR)
    img2 = cv2.imread('./input/woman.tiff', cv2.IMREAD_COLOR)

    img1_swapped = img1.copy()
    img1_swapped[:,:,0], img1_swapped[:,:,2] =\
                                        img1_swapped[:,:,2],img1_swapped[:,:,0]
    img1_blue = img1[:,:,0]
    img1_green = img1[:,:,1]
    img1_red = img1[:,:,2]
    
    cv2.imwrite('output/ps0-2-a-1.png', img1_swapped)
    cv2.imwrite('output/ps0-2-b-1.png', img1_green)
    cv2.imwrite('output/ps0-2-c-1.png', img1_red)
    cv2.imwrite('output/ps0-2-d-1.png', img1_blue)
    
    img1_mono = img1_green.copy()
    img2_mono = img2.copy(); img2_mono = img2_mono[:,:,1]
    img1_center = [dim//2 for dim in img1_mono.shape]
    img2_center = [dim//2 for dim in img2_mono.shape]
    

    img1_mono[img1_center[0]-50:img1_center[0]+50,
              img1_center[1]-50:img1_center[1]+50] = \
                      img2_mono[img2_center[0]-50:img2_center[0]+50,
                                img2_center[1]-50:img2_center[1]+50]
    img1_with_img2_crop = img1_mono
    cv2.imwrite('output/ps0-3-a-1.png', img1_with_img2_crop)
    

    min1 = np.min(img1_green)
    max1 = np.max(img1_green)
    mean = np.mean(img1_green)
    std = np.std(img1_green)
    img1_green_normed = img1_green.copy()
    img1_green_normed = cv2.add(cv2.multiply(cv2.divide(cv2.subtract(
                                        img1_green_normed,mean),std),10),mean)
    cv2.imwrite('output/ps0-4-b-1.png', img1_green_normed)
    
 
    img1_shift = img1_green_normed.copy()
    M = np.array([[1,0,-2],[0,1,0]]).astype(np.float32)
    row,col = img1_shift.shape
    img1_shift = cv2.warpAffine(img1_shift,M,(col,row))
    cv2.imwrite('output/ps0-4-c-1.png', img1_shift)
    

    img1_green_noise = img1.copy()
    noise = np.zeros(img1_green_noise.shape[:2],dtype=np.uint8)
    cv2.randn(noise,0,30)
    img1_green_noise[:,:,1] = img1_green_noise[:,:,1] + noise
    cv2.imwrite('output/ps0-5-a-1.png', img1_green_noise)
    
 
    img1_blue_noise = img1.copy()
    img1_blue_noise[:,:,0] = img1_green_noise[:,:,0] + noise
    cv2.imwrite('output/ps0-5-b-1.png', img1_blue_noise)

    tep = np.array([1,2,3,4,5])
    print(tep[-3])
    
    
    
    
    
    
    