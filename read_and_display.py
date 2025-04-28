import cv2
img = cv2.imread("./assests/mcqueen.webp")
cv2.imshow("mcqueen", img)
height = img.shape[0]
width = img.shape[1]
print("Height of Image:", height)
print("Width of Image:", width)
cv2.waitKey(0)

