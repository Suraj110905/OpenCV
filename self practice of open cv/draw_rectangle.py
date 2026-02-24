import cv2

image = cv2.imread("self practice of open cv\images\Screenshot 2025-11-17 015820.png")
print("pixels",image)
cv2.rectangle(image,(0,0),(100,100),(0,255,0),3)
cv2.imshow("rectangle image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()