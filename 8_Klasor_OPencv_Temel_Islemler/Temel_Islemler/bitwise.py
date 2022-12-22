import cv2
import numpy as np

img1=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\bitwise_1.png")
img2=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\bitwise_2.png")

#resimler uint8 veri tipine sahiptir. 
dst=cv2.addWeighted(img1,0.7,img2,0.3,0)#-->görüntüleri birbiri üzerine ağırlıkları ile eklemeişlemi yapıldı


#bit düzeyinde ve işlemleri
#img 1 ve img 2 kıyaslaması yapıldı.
#cv2.bitwise_and() : Karşılaştırılan her iki pikselde sıfırdan büyükse “True” döner.
#cv2.bitwise_or() : Karşılaştırılan piksellerden biri veya her ikisi de sıfırdan büyükse “True” döner.
#cv2.bitwise_xor() : Karşılaştırılan her iki pikselden sadece biri sıfırdan büyükse “True” döner.
#cv2.bitwise_not() : Söz konusu resimdeki piksellerin “değilini” yani tersini alır.

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