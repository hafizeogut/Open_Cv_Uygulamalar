import cv2
import numpy as np
import matplotlib.pyplot as plt
#Kontur kavramı
#nesneyi çevreleyen ard arda devam eden benzer renk özelliğine sahip olan renkler bütünüdür
#1-başla
#2-cv2.cvtColor() ile gri formata çerilir
#3-cv2.threshold() ile binary formata çevrilir
#4-cv2.findContours() kontur kordinatlarının tespiti
#5-drawContours() Bulunan noktaların çizimi

#Kontur Özellikleri

#convexhull:dışbükey örtü
img=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\map.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#img gri formata çevrildi
blur=cv2.blur(gray,(50,50))
ret,thresh=cv2.threshold(blur,75,255,cv2.THRESH_BINARY)
                        #(gray ,min,max,binary çvirme fonksiyonu 0 1 )

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#iki değer alır
                        #findContours(thresh,kontur bulma işlemini daha doğru bulmak için kullanulan iki argüman)
#print(contours) 
hull=[]

for i in range(len(contours)):#kontur değerleri tespit edildi ve listeye eklendi.
    hull.append(cv2.convexHull(contours[i],False))
    
    
background=np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)#Siyah bir tuval oluşturuldu.
for i in range(len(contours)):
    cv2.drawContours(background,contours,i,(255,0,0),3,8,hierarchy)#coun8 kesintisiz çizgi
                     
    cv2.drawContours(background,hull,i,(0,255,0),1,8,hierarchy)#hulun tuttuğu değerler çizdirildi.
#print(hull)
#0,1,2,3,4,5


titles=["orijinal","gray","blur","thresh","Image"]
images=[img,gray,blur,thresh,background]
for i in range(5):
    plt.subplot(2,3,i+1)
    #plt.subplot(satir,sutun,çizim sayısı: i+1)
    
    plt.title(titles[i])
    plt.imshow(cv2.cvtColor(images[i],cv2.COLOR_RGB2BGR))
    plt.xticks([])
    plt.yticks([])
plt.show()



"""
cv2.imshow("orijinal",img)
cv2.imshow("gray",gray)
cv2.imshow("blur",blur)
cv2.imshow("thresh",thresh)
cv2.imshow("Image",background)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()
