# load an image
# convert image into grayscale
# show and save image 
# challenges jo bhi image show hoga 1) take location input from user
                            #       2) ask user that he wants to show image or save the image.
                        #           3) if user wants to save the image then take the output name also from user
                           #           then show a message file name saved successfully
                           
                           
import cv2
image_path = input("Enter the image path")#taking location input from the user
image = cv2.imread(image_path)
if image is not None:
    cv2.imshow("Image preview",image)
    cv2.waitKey(0)
    cv2.namedWindow()
else:
    print("image not loaded")
    