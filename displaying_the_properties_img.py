import cv2
img = cv2.imread("./assests/mcqueen.webp")
cv2.imshow("cars", img)
height = img.shape[0]
width = img.shape[1]
print ("The height of the image is: ", height)
print ("The width of the image is: ", width)
cv2.waitKey(0)