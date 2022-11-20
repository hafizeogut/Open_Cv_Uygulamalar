import cv2

#capture=video yakalama
capture=cv2.VideoCapture("antalya.mp4")#Girdiğim parametrelere göre Kameramdan mı görüntü alacağız yoksa,Kayıtlı bir videodan mı onun kararını veriyoruz.

while True:#videolardan devamlı olarak  kare okuma ve gösterme

    ret,frame=capture.read()
    #videolardaki kareleri okuma
    #iki parametre döndürür
    #ret videoları doğru okudu mu ?True,False
    #frame Frameleri=kareler--> doğru okudu mu?
    if ret==0:# frameler bittiğinde ret değerim bitmediği için hata alınır
        break



    frame=cv2.flip(frame,1)#y eksenine göre tersini alıyorum
    #okuğum her bir frami ter çeviririm


    cv2.imshow("Webcam",frame)
    #cv2.waitKey(1)#her bir frame 30 mil/saniye olarak gözükür
    if cv2.waitKey(10) &0xFF==ord("q"):# klavyeden bastığım değere göre döngüyü kırqq
        break

capture.release()#video dosyası üzerindeki işlemi kapatma 
cv2.destroyAllWindows()