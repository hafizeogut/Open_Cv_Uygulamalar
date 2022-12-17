import cv2

import numpy as np

img=cv2.imread("C:\\Open_Cv_Uygulamalar\\8_Klasor_OPencv_Temel_Islemler\\Temel_Islemler\\Usak64.jpg")#resim uzantısı ile birlikte yazdırıldı

dimension=img.shape#verilen resmin şeklini boy ,en,kanal özellikleri alındı.Dimension:boyut
print(dimension)


color=img[0,150,1]#150 ,200  kordinatındaki renk değerlerini color değişkeninde tutulur.
print("BGR:",color)

blue=img[420,500,0]
print("Blue:",blue)

green=img[420,500,1]
print("Green:",green)

red=img[420,500,2]
print("Red:",red)

img[420,500,0]=20#blue değerinin renk olarak karşılığını değiştirme işlemi yapıldı
print("New Blue ",img[420,500,0])


#ıtem((150,200)kordinat,mavi)
#150 ye 200 kordinatlarındaki mavi renk değeri blue1 değişkenine atandı
blue1=img.item(150,200,0)#piksellere erişildi
print("Blue1:",blue1)


img.itemset((150,200,0),172)#pikseller değiştirildi
print("New blue2:",img[150,200,0])

cv2.imshow("Usak 64",img)


cv2.imshow("Memleket Gibi Memleket:Usak",img)#imshow(resmimin gösterileceği pencerenin adı,resmin tutulduğu değer)
cv2.waitKey(0)#bu fonksiyon girilen değer kadar ekranda tutulur mili/saniye
cv2.destroyAllWindows()#tüm pencereleri kapatmak adına önemlidir
