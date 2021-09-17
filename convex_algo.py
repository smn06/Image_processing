import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread("car.jpeg",cv2.IMREAD_COLOR)
a=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh= cv2.threshold(a,127,255,cv2.THRESH_BINARY)
contours,hier= cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

black= np.zeros_like(img)
for cnt in contours:
    epsilon=0.01*cv2.arcLength(cnt,True)
    approx=cv2.approxPolyDP(cnt,epsilon,True)
    hull=cv2.convexHull(cnt)
    cv2.drawContours(black,[cnt],-1,(0,255,0),2)
    cv2.drawContours(black,[approx],-1,(0,0,255),3)
    cv2.drawContours(black,[hull],-1,(255,0,0),4)
cv2.imshow("nn",black)
cv2.waitKey()
cv2.destroyAllWindows()