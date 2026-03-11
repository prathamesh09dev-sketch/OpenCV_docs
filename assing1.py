import cv2

path = input("Enter the image path: ")
# Image Read
image = cv2.imread(path)


if image is not None:

    # Conversion of Gray Scale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    choice = input("For Show image Enter 1 and For Save Enter 2: ")
    if choice == "1":
        cv2.imshow("Gray Scale Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == "2":
        file_name = input("Enter a file name: ")
        cv2.imwrite(file_name, gray)    
else:
    print("Could Not Load Image")