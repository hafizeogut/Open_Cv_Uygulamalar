import cv2
import numpy as np

img=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\Guzum.jpg",0)
row,col=img.shape
#satır #sütun

M = np.float32([[1,0,150],[0,1,150]])#float 32 ?

dst=cv2.warpAffine(img,M,(row,col))

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()