import cv2
import numpy as np

img=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\Guzum.jpg",0)
row,col=img.shape


#iki boyutta yön değiştirmwe işlemi uygulandı.
M=cv2.getRotationMatrix2D((col/3,row/2),188,-1)

dst=cv2.warpAffine(img,M,(col,row))

cv2.imshow("dst Halasinin Guzusu",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()