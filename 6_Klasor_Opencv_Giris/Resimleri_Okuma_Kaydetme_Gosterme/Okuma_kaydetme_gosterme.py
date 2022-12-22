import cv2 #open cv kütüphanemi cağırıldı 


img=cv2.imread("C:\\Open_Cv_Uygulamalar\\Src\\lokumum.jpg")#Dosyadaki K dosyası uzantısı belirtilerek çağırıldı
#print(img)#resmimim matematiksel ifade oldığunu gösterildi

cv2.namedWindow("image",cv2.WINDOW_NORMAL)
#cv2.namedWindow(1. paramaetre: pencere ismi,cv2.WINDOW_NORMAL)
#ikinci parametre değerim,İkinci parametre olan WINDOW_NORMAL penceremin boyutları ile oynanmasını sağlar
img=cv2.resize(img,(500,1000))

cv2.imshow("img",img)#(resmimin gösterileceği pencerenin adı,resmin tutulduğu değer)

cv2.imwrite("C:\\Open_Cv_Uygulamalar\\Output\\K1.jpg",img)#resim kaydetme işlemi
#resmi istenilen herhangi bir yere kaydetmek istersem dosya yolu belirtmem gerekir
#cv2.imwrite(yeni ad,resmin tutulduğu değişken)

cv2.waitKey(0)#bu fonksiyon girilen değer kadar ekranda tutulur mili/saniye 1 Milisaniye = 0.001 Saniye

cv2.destroyAllWindows()#tüm pencereleri kapatmak adına önemlidir