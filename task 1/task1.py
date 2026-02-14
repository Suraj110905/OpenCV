# load an image
# convert image into grayscale
# show and save image 
# challenges jo bhi image show hoga 1) take location input from user
                            #       2) ask user that he wants to show image or save the image.
                        #           3) if user wants to save the image then take the output name also from user
                           #           then show a message file name saved successfully
                           
                           
import cv2

#taking location of image input from user basically image path

image_path = input("Enter the image path")
image = cv2.imread(image_path)
choice = input("If you want to show image press 1 or for saving press 2")

#asking from user choice that if he wants to preview image or save image
if choice == '1':
   # for choice 1 previewing the image 
    if image is not None:
        cv2.imshow("Image preview",image)
        cv2.waitKey(0)
        cv2.namedWindow()
    else:
        print("image not loaded")
else:
    # for choice 2 saving the image
    if image is not None:
        output = input("Enter the output file name") #taking the saving file name input from user
        saved_image = cv2.imwrite(output,image)
        #display message and file name by which image is saved
        if saved_image:
            print("saved successfully as :",output)
        else:
            print("image not saved")
        