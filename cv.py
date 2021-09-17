import cv2
clicked=False
def onMouse(event,x,y,flags,param):
    global clicked
    if event == cv2.EVENT_FLAG_LBUTTON:
        clicked=True
    
cameraCapture=cv2.VideoCapture(0)
cv2.namedWindow('smn')
cv2.setMouseCallback('smn',onMouse)
print('camera feed showing,press any key to left')
success,frame=cameraCapture.read()
while success and cv2.waitKey(ord('a'))==-1 and not clicked:
    cv2.imshow('smn', frame)
    success,frame=cameraCapture.read()
cv2.destroyWindow('smn')
cameraCapture.release()