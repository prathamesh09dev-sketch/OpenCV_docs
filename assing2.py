import os
import cv2

folder = "images"

if not os.path.exists(folder):
    os.makedirs(folder)

path = input("Enter the image path: ")
# Image Read
image = cv2.imread(path)


if image is not None:

    choice = input("For Line Enter 1,\nFor Rectangle Enter 2,\nFor Circle Enter 3,\nFor Text Enter 4\nType: ")
    if choice == "1":
        print("Enter your (x1, y1)")
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        pt1 = (x1, y1)

        print("Enter your (x2, y2)")
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
        pt2 = (x2, y2)

        print("Enter Your BGR Color")
        B = int(input("Enter your B color: "))
        G = int(input("Enter your G color: "))
        R = int(input("Enter your R color: "))

        color = (B, G, R)
        thickness = int(input("Enter Your Thickness: "))
        cv2.line(image, pt1, pt2, color, thickness)
        show_or_save = input("For Save Enter 1,\nFor Show Enter 2\n Type Your Ans: ")
        if show_or_save == "1":
            file_name = input("Enter a file name (example: img1.jpg): ")
            file_path = os.path.join(folder, file_name)
            cv2.imwrite(file_path, image)
            print("Image saved at:", file_path)
        elif show_or_save == "2":
            cv2.imshow("Line Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    elif choice == "2":
            print("Enter your (x1, y1)")
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            pt1 = (x1, y1)

            print("Enter your (x2, y2)")
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            pt2 = (x2, y2)

            print("Enter Your BGR Color")
            B = int(input("Enter your B color: "))
            G = int(input("Enter your G color: "))
            R = int(input("Enter your R color: "))

            color = (B, G, R)
            thickness = int(input("Enter Your Thickness: "))
            cv2.rectangle(image, pt1, pt2, color, thickness)
            show_or_save = input("For Save Enter 1,\nFor Show Enter 2\n Type Your Ans: ")
            if show_or_save == "1":
                 file_name = input("Enter a file name (example: img1.jpg): ")
                 file_path = os.path.join(folder, file_name)
                 cv2.imwrite(file_path, image)
                 print("Image saved at:", file_path)
            elif show_or_save == "2":
               cv2.imshow("Rectangle Image", image)
               cv2.waitKey(0)
               cv2.destroyAllWindows()
    elif choice == "3":
            print("Enter your center (x,y)")
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            center = (x, y)
            radius = int(input("Enter your radius in degree: "))

            print("Enter Your BGR Color")
            B = int(input("Enter your B color: "))
            G = int(input("Enter your G color: "))
            R = int(input("Enter your R color: "))

            color = (B, G, R)
            thickness = int(input("Enter Your Thickness: "))
            cv2.circle(image, center, radius, color, thickness)
            show_or_save = input("For Save Enter 1,\nFor Show Enter 2\n Type Your Ans: ")
            if show_or_save == "1":
               file_name = input("Enter a file name (example: img1.jpg): ")
               file_path = os.path.join(folder, file_name)
               cv2.imwrite(file_path, image)
               print("Image saved at:", file_path)
            elif show_or_save == "2":
               cv2.imshow("Cricle Image", image)
               cv2.waitKey(0)
               cv2.destroyAllWindows()
    elif choice == "4":
            text = input("Enter Your Text: ")

            print("Enter your org (x,y)")
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            org = (x, y)
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = float(input("Enter You FontScale: "))
            print("Enter Your BGR Color")
            B = int(input("Enter your B color: "))
            G = int(input("Enter your G color: "))
            R = int(input("Enter your R color: "))

            color = (B, G, R)
            thickness = int(input("Enter Your Thickness: "))
            cv2.putText(image, text, org, font,fontScale, color, thickness)
            show_or_save = input("For Save Enter 1,\nFor Show Enter 2\n Type Your Ans: ")
            if show_or_save == "1":
               file_name = input("Enter a file name (example: img1.jpg): ")
               file_path = os.path.join(folder, file_name)
               cv2.imwrite(file_path, image)
               print("Image saved at:", file_path)
            elif show_or_save == "2":
               cv2.imshow("Added Text Image", image)
               cv2.waitKey(0)
               cv2.destroyAllWindows()
else:
    print("Could Not Load Image")