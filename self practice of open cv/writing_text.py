import cv2
image = cv2.imread("self practice of open cv\images\Screenshot 2025-11-17 015820.png")
cv2.putText(image,"hello man",(10,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow("text image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()