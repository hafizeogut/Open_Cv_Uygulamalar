import cv2 
def resize_with_Aspect_Ratio(img,width=None,height=None,inter=cv2.INTER_AREA):
#En boy oranını yeniden boyutlandırma 
#inter özelliği resmin yeniden boyulanmasında çakışma yaşamamak için kullanılır

    dimension=None #dimension=boyut
    (h,w)=img.shape[:2]#resimlerin boyutlarına ulaşmak istiyoruz.Baştan ikinciye kadar
     
    if width is None and height is None:# eğer resmin en ve boy değerleri girilmez ise alınan resmi döndür.
        return img

    if width is None :# En değeri girilmesse: boyut hesabı.
        r=height/float(h)#float şeçmemin sebebi hassas hesaplama yapılmasıdır.
        dimension=(int(w*r),height)#yeni boyut oluşturuldu.

    else:#sadece boy değeri verilirse
        r=width/float(w)
        dimension=(width,int(h*r))
    return cv2.resize(img,dimension,interpolation=inter)#inter kelime anlamı arası

img=cv2.imread("C:\\Open_Cv_Uygulamalar\\6_Klasor_Opencv_Giris\\Resimleri_Okuma_Kaydetme_Gosterme\\klon.jpg")#imread=gömmek
img1=resize_with_Aspect_Ratio(img,width=None,height=600,inter=cv2.INTER_AREA)#inter area ara alan


cv2.imshow("Original",img)#Orijinal resmimi göster
cv2.imshow("Resized",img1)#fonksiyonumun süzgecinden geçen resmi göster

cv2.waitKey(0)
cv2.destroyAllWindows()
