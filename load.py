import cv2

# Image Read
image = cv2.imread("book.jpg")

# Check a image load or not
if image is None:
    print("Error: Image not found")
else:
    print("Image loaded successfully")

# if image is not None:
#     # Image show
#     cv2.imshow("Image is Showing", image)

#     # wait key  (0) wait until anyone click in keyboard, onClick then close Windows
#     cv2.waitKey(0)

#     # Close Windows
#     cv2.destroyAllWindows()
# else:
#     print("Colud show the image")


# Image Save
# if image is not None:
#     cv2.imwrite("output.jpg", image)
#     print("Image Save Succfully")
# else:
#     print("Image is Not save")


# Image Dimension
if image is not None:
    # showing image Height, Width, Channels(color like B: Blue, G: Green, R: Red)
    h, w, c = image.shape

    print(f"Image is Loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("Could Load Image")

# Gray Scale Conversion (cvtColor is function use for image color type) use for Advantages 1. Reduce Processing time and 2. Reduce Complexcity 
if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        # Image show
    cv2.imshow("Gray Scale Image is Showing", gray)
    # wait key  (0) wait until anyone click in keyboard, onClick then close Windows
    cv2.waitKey(0)
    # Close Windows
    cv2.destroyAllWindows()


else:
    print("Could Not Load Image")
