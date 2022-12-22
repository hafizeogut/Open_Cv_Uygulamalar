import cv2

#capture=video yakalama
capture=cv2.VideoCapture("antalya.mp4")#Girilen parametrelere göre Kameradan mı görüntü alınacak yoksa kayıtlı bir videodan mı onun kararını veriliyor.

while True:#videolardan devamlı olarak  kare okuyıp ve gösterme.

    ret,frame=capture.read()
    #videolardaki kareleri okuma
    #iki parametre döndürür
    #ret videoları doğru okudu mu ?True,False
    #frame Frameleri=kareler--> doğru okudu mu?
    if ret==0:# frameler bittiğinde ret değerim bitmediği için hata alınır
        break



    frame=cv2.flip(frame,1)#y eksenine göre tersini alındı.
    #okunan her bir frame ters çevrildi.


    cv2.imshow("Webcam",frame)
    #cv2.waitKey(1)#her bir frame 30 mil/saniye olarak ayarlandı.
    if cv2.waitKey(10) &0xFF==ord("q"):# q tuşuna basıldığında çıkış sağlandı.
        break

capture.release()#video dosyası üzerindeki işlemi  release() fonksiyonu 
cv2.destroyAllWindows()