import cv2
import numpy as np

cam=cv2.VideoCapture(0)
bg=cv2.imread('./Image.jpg')

while cam.isOpened():

    ret,frame=cam.read()

    if ret:
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)   #Getting BGR to HSV
        #Getting hsv Values: lower: hue - 10, 100, 100, higher: h+10, 255, 255
        red=np.uint8([[[0,0,255]]]) #bgr value of red

        hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV) # get hsv value of red from bgr
        u_bound = np.array([10,255,255])
        l_bound = np.array([0,100,100])

        mask = cv2.inRange(hsv,l_bound,u_bound)

        # All things red
        part_1 = cv2.bitwise_and(bg , bg , mask=mask)

        mask = cv2.bitwise_not(mask)

        # All things not in red
        part_2 = cv2.bitwise_and(frame,frame,mask=mask)

        cv2.imshow("Cloak",part_1 + part_2)



        if cv2.waitKey(5) == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()

