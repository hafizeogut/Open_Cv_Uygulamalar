import cv2

img=cv2.imread("C:\\Open_Cv_Uygulamalar\\Src\\contour.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thres=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
                    #(griye çevrilen resim,min,max,binary çevirme)

M=cv2.moments(thres)#bir görüntü anı , görüntü piksellerinin yoğunluklarının belirli bir ağırlıklı ortalamasıdır ( moment )

#print(M)# key value
#Geometri Merkezi Bulunuyor.
X=int(M["m10"]/M["m00"])
Y=int(M["m01"]/M["m00"])


cv2.circle(img,(X,Y),5,(255,255,0),-1)
 #(resim,x,y kordinatları,yarıçap,renk,içi dolu)
 
 
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
 