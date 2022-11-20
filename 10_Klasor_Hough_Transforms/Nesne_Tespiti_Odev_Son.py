import cv2
import numpy as np
cap=cv2.VideoCapture(0)

lower=np.array([45,80,150]) 
upper=np.array([155,200,44])

while True:
    _,frame=cap.read() #video okuma işlemi yapıldı
    
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#bgr dan hsvye geçiş paıldı
    mask=cv2.inRange(frameHSV, lower, upper)#uper ve lower değerlerim arasında gezinme işlemi yapıldı
    
    _,thresh=cv2.threshold(mask,127,255,cv2.THRESH_BINARY)#0 1 formatında binary düzene geçildi
    
    contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#contur işlemi uyguklandı
    print(contours)
    cv2.drawContours(frame,contours,-1,(185,156,181),3)     
    
    M=cv2.moments(thresh)
    X=int(M["m10"]/M["m00"])
    Y=int(M["m01"]/M["m00"])
    cv2.circle(frame,(X,Y),5,(255,255,0),-1)#merkez noktası tespit edildi.
    
    cv2.rectangle(frame,(X-50,Y-50),(X+50,Y+50),(255,0,0),thickness=3)#dikdörtgen çizimi yapıldı.
     
    
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(25) ==ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()