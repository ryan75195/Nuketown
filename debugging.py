# create trackbars for color change
def nothing(x):
    pass

cv2.namedWindow('image')

cv2.createTrackbar('lowH','image',0,255,nothing)
cv2.createTrackbar('highH','image',255,255,nothing)
cv2.createTrackbar('lowS','image',0,255,nothing)
cv2.createTrackbar('highS','image',255,255,nothing)
cv2.createTrackbar('lowV','image',0,255,nothing)
cv2.createTrackbar('highV','image',255,255,nothing)




while(0):

    ilowH = cv2.getTrackbarPos('lowH', 'image')
    ihighH = cv2.getTrackbarPos('highH', 'image')
    ilowS = cv2.getTrackbarPos('lowS', 'image')
    ihighS = cv2.getTrackbarPos('highS', 'image')
    ilowV = cv2.getTrackbarPos('lowV', 'image')
    ihighV = cv2.getTrackbarPos('highV', 'image')

    bgr_map = cv2.imread("mapped.jpg")
    rgb_map = cv2.cvtColor(bgr_map, cv2.COLOR_BGR2RGB)
    HSV = cv2.cvtColor(rgb_map, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    mask = cv2.inRange(HSV, lower_hsv, higher_hsv)
    result = cv2.bitwise_and(rgb_map, rgb_map, mask=mask)
    cv2.imshow("result", result)
    # print )ilowH, ilowS, ilowV
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break


cv2.destroyAllWindows()
cap.release()
