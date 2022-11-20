import cv2

import numpy as np

#numPy fonksiyonlarını kulanarak bir tuval oluşturuluyor.
#canvas:tuval
canvas=np.zeros((512,512,3),dtype=np.uint8)+255#zeros() fonksiyonu için belilirli bir alanı tuval oluşturuluyor.
#zeros((boy boyutu,en boyutu,kanal:Renkli görüntü:BGR),çizim yaptığımızda kullanılan veri tipi)+matrise eklenen 255 
##print(canvas) 


#ÇİZGİ
cv2.line(canvas,(50,50),(512,512),(255,0,0),thickness=5)#Çizgi çekme işlemi yapılıyor.
#line(çizim yapacağım tuval,(Başlangıç noktası),(Son nokta),Renkdeğeri,kalınlık değeri)
cv2.line(canvas,(44,44),(64,64),(0,0,255),7)#thickness şart değildir.


#DÖRTGEN
cv2.rectangle(canvas,(80,60),(100,100),(0,255,0),thickness=2)
cv2.rectangle(canvas,(100,100),(155,155),(0,255,0),thickness=-1)

#ÇEMBER
cv2.circle(canvas,(250,250),100,(250,200,150),thickness=-1)
#cv2.circle(Tuvalim,(merkez kordinarlari),yarıcap,kalınlık)

#ÜÇGEN
p1=(200,300)
p2=(325,325)
p3=(300,200)
#çigi ile üçgen oluşturuldu.
cv2.line(canvas,p1,p2,(0,0,0),4)
cv2.line(canvas,p2,p3,(0,0,0),4)
cv2.line(canvas,p1,p3,(0,0,0),4)

#Beşgen, altıgen 
points=np.array([[512,512], [300,350], [370,380],[296,296]],np.int32)
cv2.polylines(canvas,[points],True,[100,100,100],5)
#polylines:Bir çok çizgi
#cv2.polylines(tuvalim,oluşturulan dizi değerleri:kordinatlar,şeklin kapalı açık olma durumuna göre True veya False,Renk,numPy veri tipi)


cv2.ellipse(canvas,(350,350),(100,25),10,90,360,(255,255,0),-1)
#cv2.ellipse(tuval,merkez noktası,(genişlik ve yükseklik değeri),yatay eksenle yapacağı açi,90'dan 360 derceye kadar çiz,renk,kalınlık)

cv2.imshow("Cansas",canvas)
cv2.waitKey(0)#bu fonksiyon girilen değer kadar ekranda tutulur. mili/saniye
cv2.destroyAllWindows()#pencereleri kapatmak adına önemlidir.
