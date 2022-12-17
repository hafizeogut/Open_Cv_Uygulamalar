import cv2

img=cv2.imread("C:\\Open_Cv_Uygulamalar\\6_Klasor_Opencv_Giris\\Resimleri_Okuma_Kaydetme_Gosterme\\klon.jpg")
img1=cv2.imread("C:\\Open_Cv_Uygulamalar\\Src\\g_klon.png")
img2=cv2.imread("C:\\Open_Cv_Uygulamalar\\Src\\bilateral.jpg")

#1. Ortalama Alma (Averaging)

#Blurring :Bulanıklaştırma
#her pikselin renk değerlerini çevresindeki piksellerin renk değerleriyle karıştırmaktır.
#n x n‘lik bir dizey (matris) oluşuturulmalıdır.
#soldan sağa yukarıdan aşağı doğru kayar
#Bulunduğu her bir bölgenin merkezindeki pikselin çerçevesinde bulunan piksellerin ortalamasını alır.
#işlem tüöm resim taranana kadar devam eder.
#kernel tek sayı olmak zorundaır
#kernel büyüdükçe bulanıklık artar.
#cv2.blur(kaynak resim, kernel).
blurred=cv2.blur(img,(5,5))

#2.Gaussian Yontemi
#Averaging yönteminde basitçe sadece ortalama alınır.
#Bu yöntemde ise ağırlıklı ortalama alınır
#cv2.GaussianBlur(img, (5,5),0)
gaussian_blurred=cv2.GaussianBlur(img,(5,5),0)


#3. Median Yöntemi
#Görüntüdeki gürültülere salt-pepper noise denir
#resmin üzerine dökülen tuz ve baharat görünümü
#cv2.medianBlur(kaynak resmi,kernel boyutunu) 
median_blur=cv2.medianBlur(img,3)

#4. Bilateral Yöntemi
#hem gürültüleri azaltıp hem kenarları korumak için kullanılır
#cv2.bilateralFilter(kaynak_resim, piksel_bölgesi_çapı, renk, alan)
bilateral=cv2.bilateralFilter(img2,5,40,40)


#cv2.imshow('image',img)
#cv2.imshow('blur',blurred)
#cv2.imshow('gaussian blur',gaussian_blurred)

#cv2.imshow('image g_kolon',img1)
#cv2.imshow('median blur',median_blur)


cv2.imshow('image bilateral',img2)
cv2.imshow("bilateral",bilateral)


cv2.waitKey(0)

cv2.destroyAllWindows()