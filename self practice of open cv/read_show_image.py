import cv2

image = cv2.imread("images\img5.jpg")

if image is None:
     print("image not found")
else:
     print("image loaded successfully")
cv2.imshow("image show",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
    
