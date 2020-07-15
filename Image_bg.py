import cv2

cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret,bg = cam.read()
    if ret:
        cv2.imshow("Image", bg)
        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite('Image.jpg', bg)
            break


cam.release()
cv2.destroyAllWindows()




