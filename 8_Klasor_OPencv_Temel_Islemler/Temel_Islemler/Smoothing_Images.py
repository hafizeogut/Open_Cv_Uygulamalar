import cv2
import numpy as np

img_filter=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\filter.png")
img_median=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\median.png")
img_bilateral=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\bilateral.png")

blur=cv2.blur(img_filter,(13,13))#rsemin yumşama değerini artırma
#(5,5) tek sayılar olmalıdır neden?


blur_Gaussian=cv2.GaussianBlur(img_filter,(5,5),cv2.BORDER_DEFAULT)#BORDER_DEFAULT: varsayılan kenarlık özelliği

blur_median=cv2.medianBlur(img_median,5)


blur_bilateral=cv2.bilateralFilter(img_bilateral,9,55,55)

cv2.imshow("original",img_bilateral)

#cv2.imshow("blur",blur)

#cv2.imshow("blur_Gaussian",blur_Gaussian)

#cv2.imshow("Blur median",blur_median)

cv2.imshow("Bileteral",blur_bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()