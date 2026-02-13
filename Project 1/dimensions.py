import cv2
image = cv2.imread("Project 1\image.png")
if image is not None:
    h,w,c = image.shape 
    print(f"Image loaded :\n HEIGHT :{h}\n WIDTH :{w}\n CHANNELS :{c}")
else:
    print ( "could not load image")