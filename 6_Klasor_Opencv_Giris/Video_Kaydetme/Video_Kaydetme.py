import cv2

capture=cv2.VideoCapture(0)#kamera sayısına göre değer alır 1 kamera daha olsa 0 değil 1 yazacaktım

#Video_File_Output=video dosyası çıktısı
#fileName="C:\Users\HafizeOgut\Desktop\Goruntu_Isleme\Video_Kaydetme\H.avi"
fileName="H.mp4"
codec=cv2.VideoWriter_fourcc(*'VXID')#Medya verilerindeki kodekleri 4 adet karakterle tanımlar 

frameRate=30#kare Hızı

resolition=(640,480)


Video_File_Output=cv2.VideoWriter(fileName,codec,frameRate,resolition)
#Video Dosya Çıkışı=
#1. parametrem file name: Dosya adı i
#2.paramerem codec:?
#3.parametrem frame Rate Kare hızı
#4.parametrem resolition:çözüm



while True:
    ret,frame=capture.read()#her bir frame tek tek okuma
    frame=cv2.flip(frame,1)# framelerin yönünü değiştirebiliriz
    #-1 orjine göre 
    #0 x eksenine göre
    #1 y eksenine göre yansıma yaparız

    Video_File_Output.write(frame)#framleri devamlı olaarak yazma

    cv2.imshow("Webcam Live",frame)# okuduğum frameleri gösterme
    if cv2.waitKey(1) & 0xff ==ord("q"):#1mil/saniye görmek istenilen video, q basılınca çıkılır
        break

    
Video_File_Output.release()
capture.release()#release vidoyu serbest bırakmak
cv2.destroyAllWindows()#Tüm pencereleri yok et


