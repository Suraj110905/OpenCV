import cv2
image = cv2.imread("Phase 1 (Image Handling Basics)\image.png")
if image is None:
    print("could not load image")
else:
    (h,w) = image.shape