import cv2
import numpy  as np

img=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\text.png")
img1=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\lokumum.jpg")
img1=cv2.resize(img1,(500,500))
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

gray=np.float32(gray) #fonksiyona girebilmesi için float 32 tipine çevrildi
corners=cv2.goodFeaturesToTrack(gray,50,0.01,10)
#köşe      goodFeaturesToTrack(,köşe sayısı,kalite değeri,min uzaklık,köşeler arası min mesafe)

corners=np.int0(corners)#çember çizerken float veri tipi kullanılmaz

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img1,(x,y),3,(0,0,255),-1)
    

cv2.imshow("corner",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()