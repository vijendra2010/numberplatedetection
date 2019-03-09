import cv2
import math

#videoFile = "C:\Users\vijendra singh chouh\Desktop\SIH Project\splite\Sample.mp4"

cap = cv2.VideoCapture('video7.avi')
frameRate = cap.get(5) #frame rate
x=1
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        #name = './data/frame' + str(int(x)) + '.jpg'
        #print ('Creating...' + name)
        #cv2.imwrite(name, frame)
        filename = './data/frame' +  str(int(x)) + ".jpg";x+=1
        cv2.imwrite(filename, frame)

cap.release()
print ("Done!")