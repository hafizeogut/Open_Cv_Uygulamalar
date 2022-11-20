import cv2
import numpy as np

img=cv2.imread("C:\OpenCV\OpenCv_Uygulamar_1\Src\h_line.png")
img1=cv2.imread("C:\OpenCV\OpenCv_Uygulamar_1\Src\Hough_Line_Transform.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Canny():resimlerdeki köşeleri tespit eder edges:köşeler
edges=cv2.Canny(gray,75,150)
    #     Canny(Griye çevrilen resim,başlanğıç değeri,bitiş değeri)

#cv2.HoughLines()#CPU kullanımı  fazla olduğundan
#cv2.HoughLinesP()#kullanılır


lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=1500)#Tekniğin amacı, bir oylama prosedürü ile belirli bir şekil sınıfındaki nesnelerin kusurlu örneklerini bulmaktır.
#         HoughLinesP(köşeleri bulunmuş resim,RO , teta değerleri,threshold değeri)


print(lines)


for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)#2-->15 değer büyüdükçe doğrulukta sapma yaşandı.
    
cv2.imshow("Mantık",img1)
cv2.imshow("orijinal",img)
cv2.imshow("gray",gray)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()