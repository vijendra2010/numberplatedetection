import cv2
import numpy as np
import os
import Main

# Playing video from file:
cap = cv2.VideoCapture('video7.avi')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(currentFrame<=2):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.png'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    
    # To stop duplicate images
    currentFrame += 1
    c = main.loop(currentFrame)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
