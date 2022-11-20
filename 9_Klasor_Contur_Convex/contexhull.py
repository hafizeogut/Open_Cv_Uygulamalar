import cv2
import numpy as np

#convexhull:dışnukey örtü
img=cv2.imread("C:\OpenCV\OpenCv_Uygulamar_1\Src\map.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.blur(gray,(3,3))
ret,thresh=cv2.threshold(blur,75,255,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull=[]

for i in range(len(contours)):#kontur değerleri tespit edildi ve listeye eklendi.
    hull.append(cv2.convexHull(contours[i],False))
    
    
background=np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)#Siyah bir tuval oluşturuldu.
for i in range(len(contours)):
    cv2.drawContours(background,contours,i,(255,0,0),3,8,hierarchy)#coun8 kesintisiz çizgi
    cv2.drawContours(background,hull,i,(0,255,0),1,8,hierarchy)#hulun tuttuğu değerler çizdirildi.
#print(hull)
#0,1,2,3,4,5


"""
cv2.imshow("orijinal",img)
cv2.imshow("gray",gray)
cv2.imshow("blur",blur)
cv2.imshow("thresh",thresh)
"""
cv2.imshow("Image",background)
cv2.waitKey(0)
cv2.destroyAllWindows()
