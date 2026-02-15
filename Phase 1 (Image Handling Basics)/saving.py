import cv2

image = cv2.imread("Phase 1 (Image Handling Basics)\image.png")
if image is not None:
    success = cv2.imwrite("output_image.png",image)
    if success:
        print("Image saved successfully as 'output_image.png'")
    else:
        print("Failed to save an image")
else:
    print("Error: could not load image")

