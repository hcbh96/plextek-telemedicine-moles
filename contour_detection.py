import cv2
import matplotlib.pyplot as plt
import numpy as np

i=1
while i <= 100:
    j = 1
    i = i + 5
    while j <= 100:
        j = j + 5
        # read the image
        image = cv2.imread("./images/trial4.jpeg")
        #./images/20210826_114745.jpg

        # convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        # perform edge detection
        edges = cv2.Canny(gray, i, j)



        # detect lines in the image using hough lines technique
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)




        for line in lines:
            for x1, y1, x2, y2 in line:
                print(x1, y1, x2, y2)
                cv2.line(image, (x1, y1), (x2, y2), (20, 220, 20), 3)

        # show the image
        plt.imshow(image)
        plt.savefig("./output/thes1 {} thres2 {}".format(i,j))



