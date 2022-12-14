import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("C:\\OpenCV\\OpenCv_Uygulamar_1\\Src\\Kizlarim.jpg")
#img=np.zeros((500,500),np.uint8)+50#tuval oluşturuldu
b,g,r=cv2.split(img)
plt.hist(b.ravel(),256,[0,256])#ravel()çok boyutlu dizi tek boyutlu dizi haline getirildi.
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

"""
cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)#içi dolu dökdörtgen elde edildi
cv2.rectangle(img,(250,170),(350,200),(255,255,255),-1)

"""
cv2.imshow("img",img)
#plt.hist(img.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()