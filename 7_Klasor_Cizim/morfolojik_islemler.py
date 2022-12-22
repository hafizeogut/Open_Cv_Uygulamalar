# Morfolojik(şekilbilimsel) işlemler binary resimler üzerinde çalışır

import cv2
import numpy as np
 
img=cv2.imread('C:\\Open_Cv_Uygulamalar\\Src\\dilation.PNG')
img1=cv2.imread('C:\\Open_Cv_Uygulamalar\\Src\\opening.PNG',0)
img2=cv2.imread('C:\\Open_Cv_Uygulamalar\\Src\\closing.PNG',0)
#1.Erosion
#Şekli aşındırır ve zayıflatır.
 
 
kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(img,kernel,iterations=3) 

#2.Dilation
#kelime anlamı genişlemedir
dilation=cv2.dilate(img,kernel,iterations=3)

#3.Opening
#Resim üzerindeki gürültüleri kaldırır
kernel1=np.ones((7,7),np.uint8)
opening=cv2.morphologyEx(img1,cv2.MORPH_OPEN,kernel1)

#4.Closing
#Nesnenin içindeki gürültüleri temizler
closing=cv2.morphologyEx(img2,cv2.MORPH_CLOSE,kernel1)

cv2.imshow("original image",img)
cv2.imshow("Erosion",erosion)
#cv2.imshow("dilation image",dilation)


#cv2.imshow("Original", img1)
#cv2.imshow("Opening", opening)

#cv2.imshow("origianl_clos", img2)
#cv2.imshow("Closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()