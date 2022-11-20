import cv2 
import numpy as np

circle=np.zeros( (512,512,3), np.uint8)+255#boş bir tuval oluşturuldu.
#((en,boy,kanal),veri tipi)
cv2.circle(circle,(256,256),100,(255,0,0),-1)
#center:merkezde,radius(yarıçap)=60,color:(255,0,0),içi dolu çizim

rectangle=np.zeros((512,512,3),np.uint8)+255#dörtgen olulşturuldu
cv2.rectangle(rectangle,(150,150),(350,350),(0,0,255),-1)#özellikleri girildi


add=cv2.add(circle,rectangle)#resimleri toplamak için add fonksiyonu kullanıldı
print(add)#add değeri ekranda gösterildi

print(add[256,256])#rectangle ve circle değerlerinin toplamını yazdırıldı.

cv2.imshow("Circle",circle)#içi dolu daire gösterildi
cv2.imshow("Rectangle",rectangle)#içi dolu dörtgen 
cv2.imshow("add",add)

cv2.waitKey(0)
cv2.destroyAllWindows()