import cv2
import numpy as np

img1=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\bitwise_1.png")
img2=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\bitwise_2.png")

#resimler uint8 veri tipine sahiptir.
img3=cv2.imread('C:\\Open_Cv_Uygulamalar\\Src\\Kizlarim.jpg')
img4=cv2.imread('C:\\Open_Cv_Uygulamalar\\Src\\lokumum.jpg')
dst=cv2.addWeighted(img3,0.7,img4,0.3,0)
#bit düzeyinde ve işlemleri
#img 1 ve img 2 kıyaslaması yapıldı.
bit_and=cv2.bitwise_and(img2,img1)

#bitler üzerinde or işlemi yapılıyor.
bit_or=cv2.bitwise_or(img1,img2)
bit_xor=cv2.bitwise_xor(img1,img2)
bit_not1=cv2.bitwise_not(img1)
bit_not2=cv2.bitwise_not(img2)#not bit değerlerinin tersi alınır.


cv2.imshow("Img1",img1)
cv2.imshow("Img2",img2) 
cv2.imshow("Destroy",dst)


cv2.imshow("bit_and",bit_and)
print("""
      [0,0,0]   [1,1,1]    [0,0,0]
      [1,1,1]and[1,1,1] =  [1,1,1]
      [0,0,0]   [1,1,1]    [0,0,0]
      """)

cv2.imshow("bit_and",bit_or)
print("""
      [0,0,0]   [1,1,1]    [1,1,1]
      [1,1,1]or [1,1,1] =  [1,1,1]
      [0,0,0]   [1,1,1]    [1,1,1]
      """)

cv2.imshow("bit_xor",bit_xor)
cv2.imshow("bit_not1",bit_not1)
cv2.imshow("bit_not1",bit_not2)

cv2.waitKey(0)
cv2.destroyAllWindows()