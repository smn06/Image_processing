import cv2
import numpy as np

cir=cv2.imread('hammer.png')
grays=cv2.cvtColor(cir,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(grays,5)
circle=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=0)
circles=np.uint32(np.around(circle))

for i in circles[0,:]:
    cv2.circle(cir,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(cir,(i[0],i[1]),2,(0,0,255),3)

cv2.imwrite("hammer.png",cir)
cv2.imshow("houghcircles",cir)
cv2.waitKey()
cv2.destroyWindow()