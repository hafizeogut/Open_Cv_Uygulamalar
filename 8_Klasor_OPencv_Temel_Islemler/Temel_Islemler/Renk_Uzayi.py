import cv2

img=cv2.imread("Usak64.jpg")


img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#görüntülerin renk uzayını değiştirmek için cvtColor fonksiyonu kullanıldı
#COLOR_BGR2RGB :BGR renk uzaynı RGB uzayına çevrildi
#OpenCv BGR formatta çalışır. Matplotlip RGB formatta çalışır bu farklı kullanımıın sebebi nedir?
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#BGR-->HSV dönüşümü yapıldı
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#BGR-->GRAY dönüşümü yapıldı

cv2.imshow("USAK BGR",img)
cv2.imshow("USAK RGB",img_rgb)
cv2.imshow("USAK HSV",img_hsv)
cv2.imshow("USAK Gray",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()