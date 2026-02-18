import cv2

image = cv2.imread("images\img5.jpg")

cv2.rectangle(image,(50,50),(100,100),(0,255,0),3)
cv2.imshow("rectangle image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()