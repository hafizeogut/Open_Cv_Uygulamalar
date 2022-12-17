import cv2 
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8)+255#numPy kütüphanesinin içine girerek belirtilen boyutlarda bir tuval oluşturdum
#+255 matrislerde toplama :tüm değerlere 255 eklendi
cv2.imshow("canvas",canvas)
#(Tuvalin gösterileceği pencerenin adı,Tuval)

cv2.waitKey(0)# Tuval girilen değer kadar ekranda tutulur mili/saniye.

cv2.destroyAllWindows()# tüm pencereleri kapatmak adına önemlidir


print(canvas)#oluşturduğum değerler aslında arkada matris yazdırıldı