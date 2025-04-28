import cv2
img = cv2.imread("./assests/mcqueen.webp")
cv2.imshow("./assests/mcqueen.webq", img)
cv2.imwrite("./assests/mcqueen.png", img)
cv2.imwrite("./assests/mcqueen.tiff", img)
cv2.imshow("./assests/mcqueen.png", img)
cv2.imshow("./assests/mcqueen.tiff", img)
cv2.waitKey(0)

