import cv2
import numpy as np

capture=cv2.VideoCapture("C:\\Open_Cv_Uygulamalar\\Src\\dog.mp4")

while(1):
    _,frame=capture.read()#_True False feğeri dödürür
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#renk uzayı değiştirildi
    sensitivity=15
    lower_white=np.array([0,0,255-sensitivity])#hsv code for *white
    upper_white=np.array([255,sensitivity,255])
    
    mask=cv2.inRange(hsv,lower_white,upper_white)#iki değer arası maske oluşturma işlemi yapıldı.
    res=cv2.bitwise_and(frame,frame,mask=mask)#bitwise ikili bir döngü olması gereği iki kere frame alınır.
    #maskın doğru uygulanabilmesi için oluşturuldu
    #cv2.bitwise_and(frame,frame)
    #.1 frame de video var 2.framede kazınmış maslke uygulanmış görüntü saklanır.
    cv2.imshow("frame",frame)
    cv2.imshow("frame",mask)
    cv2.imshow("result",res)
    
    k=cv2.waitKey(5) & 0xFF 
    if k==27:
        break
cv2.destroyAllWindows()