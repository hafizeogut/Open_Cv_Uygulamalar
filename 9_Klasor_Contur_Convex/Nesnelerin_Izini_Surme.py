import cv2
import numpy as np

capture=cv2.VideoCapture("C:\\OpenCV\\OpenCv_Uygulamar_1\\8_Klasor_OPencv_Temel_Islemler\\Video_Renk_Uzay_Degistirme\\Kara_Sevda1.mp4")

while(1):
    _,frame=capture.read()#_True False feğeri dödürür
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    sensitivity=15
    lower_white=np.array([0,0,255-sensitivity])#hsv code for *white
    upper_white=np.array([255,sensitivity,255])
    
    mask=cv2.inRange(hsv,lower_white,upper_white)
    res=cv2.bitwise_and(frame,frame,mask=mask)#bitwise ikili bir döngü olması gereği iki kere frame alınır
    #cv2.bitwise_and()
    cv2.imshow("frame",frame)
    cv2.imshow("frame",mask)
    cv2.imshow("result",res)
    
    k=cv2.waitKey(25) & 0xFF 
    if k==25:
        break
cv2.destroyAllWindows()