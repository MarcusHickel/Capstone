#!/usr/bin/python

# Standard imports
import cv2
import numpy as np

# Read image
# im = cv2.imread("/home/marcus/rockettrackingplatform/Blobdetect/image3.png")
im = cv2.imread("/home/marcus/rockettrackingplatform/Blobdetect/hsvmap.png")
# im = cv2.imread("/home/marcus/rockettrackingplatform/Blobdetect/blob.jpg")

hue_min = np.array([5, 20, 20],np.uint8)
hue_max = np.array([20, 255, 255],np.uint8)

hsv_img = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)

frame_threshed = cv2.inRange(hsv_img, hue_min, hue_max)
masked = cv2.bitwise_and(im,im,mask=frame_threshed)
# cv2.imwrite('output2.jpg', frame_threshed)
frame_threshed = cv2.bitwise_not(frame_threshed)
cv2.imshow("threshold", frame_threshed)
cv2.imshow("mask",masked)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Filter by Area.
params.filterByArea = True
params.minArea = 5

# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87
    
# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.1

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(frame_threshed)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)