import cv2
img=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\contour.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)#min ve max threshol değerleri 2 ve üçüncü parametrelerimi oluşutur

counturs,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt=counturs[0]
M=cv2.moments(cnt)
#print(M)
area=cv2.contourArea(cnt)
print(area)
print(M['m00'])

perimeter_cevre=cv2.arcLength(cnt,True)#true şeklin içi dolu mu?
print(perimeter_cevre)

cv2.imshow("original",img)
cv2.imshow("gray",gray)
cv2.imshow("threshold",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()