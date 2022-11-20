import cv2
import numpy as np

img=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\yavrucuklarim.jpg",0)
img=cv2.resize(img,(590,400))

#matris değerleri
kernel=np.ones((4,4),np.uint8)
erosion=cv2.erode(img,kernel,iterations=2)

dilation=cv2.dilate(img,kernel,iterations=1)

opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
gardient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
Tophet=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
#kalınlaştırma

cv2.imshow("img original:yavrularim",img)

#cv2.imshow("erosion",erosion)

#cv2.imshow("dilation",dilation)

#cv2.imshow("morphologyEx",closing)#gürültü silinir

#cv2.imshow("closing",opening)
cv2.imshow("closing",gardient)#dış kısmımın çizimi iç kısmın siyah yapıldı
cv2.imshow("closing",Tophet)

cv2.waitKey(0)
cv2.destroyAllWindows()