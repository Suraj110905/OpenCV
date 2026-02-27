import cv2
image = cv2.imread("self practice of open cv\images\Screenshot 2025-11-17 015820.png")
cv2.circle(image,(40,40),20,(0,0,255),-1)

cv2.imshow("circle image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()