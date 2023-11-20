import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    _,img = cap.read()
    img = cv2.flip(src=img, flipCode=1)
    
    img_hsv = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2HSV)
        

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(src=img_hsv, lowerb=lower_red, upperb=upper_red)

    res = cv2.bitwise_and(src1=img, src2=img, mask=mask)


    cv2.imshow("img", img)
    
    cv2.imshow("result", res)

  
    cv2.waitKey(1)