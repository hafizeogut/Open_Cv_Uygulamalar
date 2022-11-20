import cv2
import numpy as np

capture=cv2.VideoCapture(0)#görüntü webcamden alındı.

#trackbar oluşturma işlemi yapıldı

def nothing(x):
    pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",500,500)#trakbarın boyuları oluşturuldu
#Lower: Alt değerler
#resize: frame ve görüntüleri yeniden boyutlandırm

cv2.createTrackbar("Lower - H","Trackbar",0,180,nothing)
#izleme çubuğu oluştur(hue:renk,  0,180 değer aralığında:,)
cv2.createTrackbar("Lower - S","Trackbar",0,255,nothing)#saturation :doygunluk
cv2.createTrackbar("Lower - V","Trackbar",0,255,nothing)#value: değer

#Lower: Üst değerler
cv2.createTrackbar("Upper - H","Trackbar",0,180,nothing)
cv2.createTrackbar("Upper - S","Trackbar",0,255,nothing)
cv2.createTrackbar("Upper - V","Trackbar",0,255,nothing)
#Lower---------trackbar------------>Upper

#trackbar varsayılan olarak 0 'dan başlar fakat alt kızakların sonda olması daha mantılıdır.
cv2.setTrackbarPos("Upper - H","Trackbar",180)
cv2.setTrackbarPos("Upper - S","Trackbar",255)
cv2.setTrackbarPos("Upper - V","Trackbar",255)

while True:
    ret,frame=capture.read()#kameradan alınan görüntü okundu
    frame=cv2.flip(frame,1)#görüntünün y eksen,ne göre yansıması alındı

    frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#alınan frameler Hsv formatına çevrildi
    #üst kızaklar oluşturuluyor
    Lower_H=cv2.getTrackbarPos("Lower - H","Trackbar")
    Lower_S=cv2.getTrackbarPos("Lower - S","Trackbar")
    Lower_V=cv2.getTrackbarPos("Lower - V","Trackbar")

    #alt kızaklar oluşturuluyor
    Upper_H=cv2.getTrackbarPos("Upper - H","Trackbar")
    Upper_S=cv2.getTrackbarPos("Upper - S","Trackbar")
    Upper_V=cv2.getTrackbarPos("Upper - V","Trackbar")


    #üst renk değerlerini lower_color değişkenine dizi olarak atanıyor
    lower_color=np.array([Lower_H,Lower_S,Lower_V])

    #alt renk değerlerini upper_color değişkenine dizi olarak atanıyor
    upper_color=np.array([Upper_H,Upper_S,Upper_V])

    mask=cv2.inRange(frame_hsv,lower_color,upper_color)

    cv2.imshow("Original",frame)
    cv2.imshow("Mask",mask)

    if cv2.waitKey(20) & 0xFF==ord("q"): #20 fbs değeri
        break


capture.release()#görüntü serbest bırakıldı
cv2.destroyAllWindows()#Tüm pencereleri kapat



