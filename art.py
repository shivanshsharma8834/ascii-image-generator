import cv2
import numpy as np
import sys 

symbol_list = ["#","-","*",".","+","o","=","%","&","$","@"]
threshhold_list = [0, 20, 40, 60, 80,100,120,140,160,180,200]

def print_out_ascii(array):

    for row in array:
        for e in row:
            print(symbol_list[int(e) % len(symbol_list)],end="")
        print()


def img_to_ascii(image):

    height,width = image.shape
    new_width = int(width/3)
    new_height = int(height/3)

    resized_image = cv2.resize(image, (new_width,new_height))

    thresh_image = np.zeros(resized_image.shape)

    for i, threshold in enumerate(threshhold_list):
        thresh_image[resized_image > threshold] = i

    return thresh_image


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Image path not specified :")
        exit()

    if len(sys.argv) == 2:
        print("Using {} as Image: \n".format(sys.argv[1]))
        image_path = sys.argv[1]

    image = cv2.imread(image_path,0)

    ascii_art = img_to_ascii(image)
    print_out_ascii(ascii_art)



