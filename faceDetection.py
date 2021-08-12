import cv2 as cv

image = cv.imread("photos/join.jpg")
cv. imshow("people", image)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)


#Reading haarcascade file
haar_cascade = cv.CascadeClassifier("har_face.xml")

faces_rectangle = haar_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors = 9) #Increase miniNeighbors to reduce noise
print(f"Number of faces found = {len(faces_rectangle)}")

#drawing rectangles over the detected faces
for (x,y,w,h) in faces_rectangle:
    cv.rectangle(image, (x,y), (x+w,y+h), (0,255,0),thickness = 2)
cv.imshow("detected faces", image)


cv.waitKey(0)