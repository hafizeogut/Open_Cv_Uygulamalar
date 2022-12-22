import cv2

#capture=video yakalama
capture=cv2.VideoCapture(0)#Girilen parametrelere göre Kameramdan mı görüntü alınacak yoksa kayıtlı bir videodan mı?

while True:#videolardan devamlı olarak  kare okuma ve gösterme
    ret,frame=capture.read()#videolardaki kareleri okuma
    #iki parametre döndürür
    #ret videoları doğru okudu mu ?True,False
    #frame Frameleri=kareler--> doğru okudu mu?

    frame=cv2.flip(frame,1)#y eksenine göre tersini alıyorum
    #okuğum her bir frami ter çeviririm


    cv2.imshow("Webcam",frame)
    #cv2.waitKey(1)#her bir frame 30 mil/saniye olarak görünür
    if cv2.waitKey(1) &0xFF==ord("q"):# klavyeden bastığım değere göre döngüyü kırıp durdurma işlemi yapıldı.
        break

capture.release()#video dosyası üzerindeki işlemi kapatma 
cv2.destroyAllWindows()