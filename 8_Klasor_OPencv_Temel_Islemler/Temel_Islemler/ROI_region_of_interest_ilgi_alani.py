#roi region of interest:ilgi alanı
import cv2

img=cv2.imread("Beyzam.jpg")
print(img.shape[:2])#resmin şekli en ve boy :kanal boyutu alınmadı

roi=img[30:200,200:400]#belli kordinatlarda ilgi alanı oluşturuldu
       #[   y  , x     ]
cv2.imshow("Beyzam:30.10.2022",img)
cv2.imshow("ROI",roi)


cv2.waitKey(0)
cv2.destroyAllWindows()