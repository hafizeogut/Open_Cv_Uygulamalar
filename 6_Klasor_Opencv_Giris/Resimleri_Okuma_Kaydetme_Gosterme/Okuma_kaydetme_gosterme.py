import cv2 #open cv kütüphanemi cağırıldı 


img=cv2.imread("K.jpg")#Dosyadaki K dosyası uzantısı belirtilerek çağırıldı
#print(img)#resmimim matematiksel ifade oldığunu gösterildi

cv2.namedWindow("image",cv2.WINDOW_NORMAL)
#cv2.namedWindow(1. paramaetre: pencere ismi,cv2.WINDOW_NORMAL)
#ikinci parametre değerim,İkinci parametre olan WINDOW_NORMAL penceremin boyutları ile oynanmasını sağlar


cv2.imshow("img",img)#(resmimin gösterileceği pencerenin adı,resmin tutulduğu değer)

cv2.imwrite("K1.jpg",img)#resim kaydetme işlemi
#resmi istenilen herhangi bir yere kaydetmek istersem dosya yolu belirtmem gerekir

cv2.waitKey(0)#bu fonksiyon girilen değer kadar ekranda tutulur mili/saniye

cv2.destroyAllWindows()#tüm pencereleri kapatmak adına önemlidir