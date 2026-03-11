import cv2

# Image Read
image = cv2.imread("book.jpg")

# Resizing image (changing a size of image)
# resized = cv2.resize(src, dsize, fx, fy, interpolation)

# if image is None:
#     print("Image is not found")
# else:
#     print("Image is loaded")

#     resized = cv2.resize(image, (300, 300))
#     # 1st width and then hight 

#     cv2.imshow("Original Image is showing", image)
#     cv2.imshow("ReSized Image is showing", resized)
#     cv2.imwrite("resized_image.png", resized)  ## Save image
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# Croping Image using slicing in OpenCV
# cropped_image = image[startY:endY, startX:endX]

# if image is not None:
#     cropped_image = image[200:500, 500:600]
#     # In Y axis betwwen 200 to 500 pixel and In X axis between 500 to 600 pixel

#     cv2.imshow("Original Image is showing", image)
#     cv2.imshow("Cropped Image", cropped_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# Image Rotation And Flipping

# Image Rotation
# M = cv2.getRotationMatrix2D(center, angle, scale)
# rotated_image = cv2.warpAffine(image, M, (width, height))

# if image is None:
#     print("Image is not Load")
# else:
#     # Uisng shape attribute find hight and width
#     (h, w) = image.shape[:2]  #show 2 value

#     # clockwise 
#     center = (w//2, h//2)
#     M = cv2.getRotationMatrix2D(center, 90, 1.0)  #1.0 is scaleg
#     roated = cv2.warpAffine(image, M, (w, h))
    
#     cv2.imshow("Original Image is showing", image)
#     cv2.imshow("Rotated 90 degree Image", roated)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# Image Flipping
# if image is None:
#     print("Image is not Load")
# else:
#     flipped_horizontal = cv2.flip(image,1)
#     flipped_vertical = cv2.flip(image,0)
#     flipped_both_side = cv2.flip(image,-1)

#     cv2.imshow("Original Image is showing", image)
#     cv2.imshow("Iflipped_horizontal mage is showing", flipped_horizontal)
#     cv2.imshow("flipped_vertical Image is showing", flipped_vertical)
#     cv2.imshow("flipped_both_side Image is showing", flipped_both_side)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# Image Transformation & Manipulation

# Drawing Line
# cv2.line(image, pt1, pt2, color, thickness)
# if image is None:
#     print("Image is not Load")
# else:
#     print("Image loaded sussfully")

#     pt1 = (300,200)
#     pt2 = (900,200)
#     color = (255, 0 , 0)
#     thickness = 4

#     cv2.line(image, pt1, pt2, color, thickness)
#     cv2.imshow("Line Image is showing", image)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# Drawing Reactangle 
# cv2.rectangle(image, pt1, pt2, color, thickness)
# pt1 is top left corner and pt2 is bottom right corner
# if image is None:
#     print("Image is not Load")
# else:
#     print("Image loaded sussfully")

#     pt1 = (200,200)
#     pt2 = (900,700)
#     color = (0, 0 , 255)
#     thickness = 3

#     cv2.rectangle(image, pt1, pt2, color, thickness)
#     cv2.imshow("Rectangle drow Image is showing", image)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()



# Drawing Cricle
# cv2.circle(image, center, radius, color, thickness)
# if image is None:
#     print("Image is not Load")
# else:
#     print("Image loaded sussfully")
#     center = (500,300)
#     radius = 200
#     color = (0, 0 , 255)
#     thickness = -1  # -1 fill circle using given color

#     cv2.circle(image, center, radius, color, thickness)
#     cv2.imshow("Circle drow Image is showing", image)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# Adding Text
# cv2.putText(image, text, org, font, fontScale, color thickness)
if image is None:
    print("Image is not Load")
else:
    print("Image loaded sussfully")
    text = "Book in Lib"
    org = (50,200)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1.2
    color = (255, 0, 0)
    thickness = 2

    cv2.putText(image, text, org, font, fontScale, color, thickness)
    cv2.imshow("Add text drow Image is showing", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()