import cv2
import numpy as np

Capture=cv2.VideoCapture("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\line.mp4")


#https://towardsdatascience.com/lines-detection-with-hough-transform-84020b3b1549

while True:
    ret,frame=Capture.read()
    Capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
    Capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#hsv range for
    lower_yellow=np.array([18,94,140],np.uint8)#en yüksek değer
    upper_yellow=np.array([48,255,255],np.uint8)#en düşük değer

    
    mask=cv2.inRange(hsv,lower_yellow,upper_yellow)
    edges=cv2.Canny(mask,75,250)
    
    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)
    for line in lines:
        (x1,y1,x2,y2)=line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
        
    
    
    cv2.imshow("edg",frame)
    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

Capture.release()
cv2.destroyAllWindows()