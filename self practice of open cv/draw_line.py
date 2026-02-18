import cv2
image = cv2.imread("images\img5.jpg")

cv2.line(image,(0,0),(200,200),(0,0,255),100)

cv2.imshow("line image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()