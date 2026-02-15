import cv2

image = cv2.imread("Phase 1 (Image Handling Basics)\image.png")

if image is None:
    print("image not found")
else:
    print("image loaded successfully")
    
    resized = cv2.resize(image ,(300,300))
    
    cv2.imshow("original image",image)
    cv2.imshow("resized image",resized)
    
    cv2.imwrite("output_resized.png",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    