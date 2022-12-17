import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=np.zeros((400,400),np.uint8)
white=(255,255,255)
cv2.rectangle(img1,(75,75),(325,325),white,-1)
cv2.imshow("Rectangle",img1)

img2=np.zeros((400,400),np.uint8)
cv2.circle(img2,(200,200),175,white,-1)
cv2.imshow("Circle",img2)

bitwiseAnd=cv2.bitwise_and(img1,img2)
bitwiseOr=cv2.bitwise_or(img1,img2)
bitwiseXor=cv2.bitwise_xor(img1,img2)
bitwiseNot=cv2.bitwise_not(img2)


titles = ["Rectangle", "Circle", "Bitwise And", "Bitwise Or", "Bitwise Xor", "Bitwise Not"]
images = [img1, img2, bitwiseAnd, bitwiseOr, bitwiseXor, bitwiseNot]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(cv2.cvtColor(images[i],cv2.COLOR_RGB2BGR))
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()