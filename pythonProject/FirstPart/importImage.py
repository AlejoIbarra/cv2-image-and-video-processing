import cv2
print("package imported")

img = cv2.imread("../Resources/img/woman.jpg")

#the first one is the name of te window
cv2.imshow("Output",img)
#agregate delay

cv2.waitKey(0)