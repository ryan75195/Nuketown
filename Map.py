import cv2
import numpy as np
import pygame

def nothing(x):
    pass


cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)

cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)


while True:

    map = cv2.imread("mapped.jpg")
    hsv = cv2.cvtColor(map, cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos("LH", "Tracking")
    ls = cv2.getTrackbarPos("LS", "Tracking")
    lv = cv2.getTrackbarPos("LV", "Tracking")

    uh = cv2.getTrackbarPos("UH", "Tracking")
    us = cv2.getTrackbarPos("US", "Tracking")
    uv = cv2.getTrackbarPos("UV", "Tracking")

    LB = np.array([lh,ls,lv])
    UB = np.array([uh,us,uv])
    mask = cv2.inRange(hsv, LB, UB)

    res = cv2.bitwise_and(map, map, mask=mask)
    cv2.imshow("Image", map)
    cv2.imshow("res", res)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# class Map:

    #
    # walls = np.array((0,255,0))
    # jumpabables = np.array((0,0,255))
    # conditional_jumpables = np.array((255,0,255))
    # Height_Change = np.array((0,255,255))
    # buildings = np.array((255,0,0))
    # heights_dependant_exits = np.array((255,255,0))
    #
    # lower = np.array((255,254,60))
    # upper = np.array((255,255,100))
