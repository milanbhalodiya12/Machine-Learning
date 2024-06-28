To get face detection xml file downloade the following from given link : 
https://github.com/opencv/opencv/tree/master/data/haarcascades




import cv2

img = cv2.imread("4.png", cv2.IMREAD_COLOR)

face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face.detectMultiScale(grey, 1.1, 4)
print(faces)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),3)

cv2.imshow("Face Detector",img)
cv2.waitKey(50000)
cv2.destroyAllWindows()







