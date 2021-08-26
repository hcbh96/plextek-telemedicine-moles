# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 10:35:42 2021

@author: tr
"""

import numpy as np
import cv2
import random

def detect_shape(img):
#    img = cv2.imread('shapes.png')

    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thrash = cv2.threshold(imgGry, 180, 255, cv2.THRESH_BINARY)
    contours , _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


    shapeDetected = False

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        if len(approx) == 3:
            cv2.putText( img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0) )
        elif len(approx) == 4:
            x, y , w, h = cv2.boundingRect(approx)
            if w>5 and h>5: # Make adaptive
                aspectRatio = float(w)/h
                cv2.drawContours(img, [approx], 0, (255, 0, 0), 5)
                if aspectRatio >= 0.95 and aspectRatio < 1.05:
                    cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                    shapeDetected = True

                else:
                    cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                    shapeDetected = True

        elif len(approx) == 5 :
            cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        # elif len(approx) == 10 :
        #     cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        # else:
        #     cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    #
    if shapeDetected:
        final_img = cv2.imwrite("./output/{}.jpg".format(random.random()), img)


    cv2.destroyAllWindows()



