import cv2
import numpy as np
from matplotlib import pyplot as plt
#from:organ import:doku
#Thersholding:nesne ve arka planı birbirinden ayırma...
img=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\Guzum.jpg",0)
# 0 değeri siyah beyaz:grayscale

ret,th1=cv2.threshold(img,85,225,cv2.THRESH_BINARY)

th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)
#retrun,thresholding

th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,41,2)



cv2.imshow("image",img) 
#cv2.imshow("image-th 1",th1) 

#cv2.imshow("image-th 2",th2) 

cv2.imshow("image-th 3",th3) 
cv2.waitKey(0)
cv2.destroyAllWindows()
