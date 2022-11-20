import cv2

capture=cv2.VideoCapture("C:/Users/HafizeOgut/OneDrive/Masaüstü/Goruntu_Isleme/8_Klasor_OPencv_Giris/Video_Renk_Uzay_Degistirme/Kara_Sevda1.mp4")#Video işleme  yapıldı
 
while True:
    ret,frame=capture.read()#read() hem frameleri, hemde true ,false değerlerini döndürür
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#videodan aldığım frameleri BGR DAN GRAY E çevrildi
    if ret==False:
        break
    
    cv2.imshow("Kara Sevda",frame)

    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
