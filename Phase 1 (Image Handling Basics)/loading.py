import cv2

image = cv2.imread("Project 1\image.png")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")