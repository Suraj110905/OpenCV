import cv2

image = cv2.imread("Phase 1 (Image Handling Basics)\image.png")

if image is not None:
    cv2.imshow("Image preview",image) #open the window for showing image
    cv2.waitKey(0) #wait for a key press by user
    cv2.namedWindow() #close the window when user press a key
else:
    print("Image Not loaded")