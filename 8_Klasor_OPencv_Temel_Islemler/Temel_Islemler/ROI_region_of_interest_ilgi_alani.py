#roi region of interest:ilgi alanı
import cv2

img=cv2.imread("C:\\Open_Cv_Uygulamalar\\Src\\Guzum.jpg")
print(img.shape[:2])#resmin şekli en ve boy :kanal boyutu alınmadı

roi=img[20:350,350:400]#belli kordinatlarda ilgi alanı oluşturuldu
       #[   y  , x     ]
cv2.imshow("Guzum",img)
cv2.imshow("ROI",roi)


cv2.waitKey(0)
cv2.destroyAllWindows()