import cv2

#cv2.namedWindow("Klon",cv2.WINDOW_NORMAL)#WINDIW_NORMAL ile boyutlandırma yaptık

img=cv2.imread("C:\\Open_Cv_Uygulamalar\\Src\\Kizlarim.jpg")#Dosya Yolu verilerek resim içe aktarıldı.
print(img)

img=cv2.resize(img,(400,480))

cv2.imshow("Usak Kuzulari",img)
cv2.waitKey(0)
cv2.destroyAllWindows()