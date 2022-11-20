import cv2
import numpy as np

img1=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\coins.jpg")#resimlere ulaşıldı ve yazdırıldı
img2=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\balls.jpg")


#resimler gray çevirme işlemi :
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img1_blur=cv2.medianBlur(gray1,5)#cernel size
img2_blur=cv2.medianBlur(gray2,5)

circles=cv2.HoughCircles(img1_blur,cv2.HOUGH_GRADIENT,1,img1.shape[0]/4,param1=200,param2=10,minRadius=20,maxRadius=89)
#               (blurlu resim,algılama yöntemi,çöünürlük oranı,img shape hesabı,param1=200 olmalıdır gradient,thershol değeri,çemberlerin min yarıçağı,max,yarıçapı)



if circles is not None:#Circles içeriği boş değilse
    circles=np.uint16(np.around(circles)) #16 8 tutuğu aralığı artıtıp azaltmak adına önemlidir.
    for i in circles[0,:]:#circle 0 dan sonuna kadar tutulan dizimin içerisinde geziniliyor
        cv2.circle(img1,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(img1,(i[0],i[1]),2,(0,0,255),3)
    
cv2.imshow("img1",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()