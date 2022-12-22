
import cv2
import numpy as np

canvas=np.zeros((600,600,3),dtype=np.uint8)+255#yazı yazılacak bir zemin oluşturukldu

font1=cv2.FONT_HERSHEY_COMPLEX_SMALL
font2=cv2.FONT_HERSHEY_COMPLEX
font3=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX

cv2.putText(canvas,"OpenCv",(60,60),font1,4,(0,0,0),cv2.LINE_8)

cv2.putText(canvas,"OpenCv",(0,200),font2,5,(125,25,65),cv2.LINE_AA)

cv2.putText(canvas,"OpenCv",(20,333),font3,1,(0,0,0),cv2.LINE_4)


cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()