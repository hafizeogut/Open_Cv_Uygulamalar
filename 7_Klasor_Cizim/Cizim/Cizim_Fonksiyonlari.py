import cv2

import numpy as np

#numPy fonksiyonlarını kulanarak bir tuval oluşturuluyor.
#canvas:tuval
canvas=np.zeros((512,1000,3),dtype=np.uint8)#zeros() fonksiyonu için belilirli bir alanı tuval oluşturuluyor.
#zeros((boy boyutu,en boyutu,kanal:Renkli görüntü:BGR),çizim yaptığımızda kullanılan veri tipi)
print(canvas)#siyah bir tuvalin matris değerleri yazdırılıyor.

cv2.imshow("canvas",canvas)
cv2.waitKey(0)#bu fonksiyon girilen değer kadar ekranda tutulur. mili/saniye
cv2.destroyAllWindows()#pencereleri kapatmak adına önemlidir.

