import cv2

img=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\contour.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,Treshold=cv2.threshold(gray,12,255,cv2.THRESH_BINARY)
M=cv2.moments(Treshold)
#print(Treshold)
#print(M)# key value

#Geometri Merkezi Bulunuyıor
X_Kordinati=int(M['m10']/M['m00'])
Y_Kordinati=int(M['m01']/M['m00'])

cv2.circle(img,(X_Kordinati,Y_Kordinati),5,(0,255,0)-1)


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()