#Kontur:şeklin sınırları boyunca ard arda devam eden benzer renk özelliğine  sahip olan renk bütünüdür
#       Temel Kontur Tespit Algoritması
#Yüksek doğruluklu kontur çizimleri için binary resimler kulllanmalıyız cv2.cvtColor() cv2. trreshold()
#kontur kordinatları tespiti cv2.findContours
#bulunan noktaların tespiti cv2.drawContours
# Contous Features:Kontur Ozellikleri
#   Alan
#   Çevre
#   geometri merkezi
#   Çevreleyici Geometriler

#convex hull Duşbükey Örtü
#Convex Hull:Dışbükey örtü
#Convexity Defects:Dışbükey 

import cv2 
img=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\contour1.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#resmin gri tonlara çevrilme işlemi yapılsı

ret,tresh=cv2.threshold(gray,12,255,cv2.THRESH_BINARY)#ya siyah ya beyaz
contours,_=cv2.findContours(tresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#fonksiyonum iki değer alır
                            #(tresh ,yapılan kontur bulma işlemini daha doğru bulma için kullanılan iki parametre)
#print(counours)#sözlük:Görüntülerin olduğu bir sözlük. 
# bulunan kordinatlar yazdırıldı

cv2.drawContours(img,contours,-1,(0,0,255),3)
                #(resim,kullanılacak kordinatlar,-1,renkk,kalınlık) 
                                            #-1 ,0,1 değeri alır
#cv2.drawContours(img,contours,1,(0,0,255),3) şeklin etrafını çizer
#-1 hem şeklin hem çereçevenin
#0 sadece çerçevenin etrafını çizer

cv2.imshow("contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()