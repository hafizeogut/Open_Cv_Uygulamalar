

import cv2
cap=cv2.VideoCapture(0)

while 1:
    ret,frame=cap.read()#ret true false değeri döndürür
    frame=cv2.flip(frame,1)#görüntüyü takla attırıldı.
    #1 girildiğinde y eksenine göre görüntünün tersini veriliyor
    
    edges=cv2.Canny(frame,100,200)#kenarlık cizdiriliyor.,
    #cv2.Canny(input,minThreshold,maxThreshold)
    
    cv2.imshow("frame",frame)
    cv2.imshow("Edges",edges)
    
    
    if cv2.waitKey(5) & 0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()