import cv2
import numpy as np
import math
# Read image
im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)
def getFilter(minThreshold = 90, maxThreshold = 200, minCircularity = 0, maxCircularity = 1, minConvexity = 0, maxConvexity = 0.95, minInertiaRatio = 0.5):
    params = cv2.SimpleBlobDetector_Params()

    params.filterByArea = False
    params.minArea = 100

    # Change thresholds
    params.minThreshold = minThreshold
    params.maxThreshold = maxThreshold

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = minCircularity
    params.maxCircularity = maxCircularity

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = minConvexity
    params.maxConvexity = maxConvexity

    params.filterByInertia = False
    params.minInertiaRatio = minInertiaRatio
    return params


def getTriangleFilter():
    return getFilter(90, 200, 0.3, 0.7, 0, 1)

def getPointyFilter():
    return getFilter(90, 200, 0, 0.4, 0, 0.65, 0.3)

def getCircleFilter():
    return getFilter(90, 200, 0.7, 1.0, 0, 1)

def detectWithFilter(filter):
    detector = cv2.SimpleBlobDetector(filter)
    keypoints = detector.detect(im)
    print (keypoints)
    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)

while True:
    detectWithFilter(getPointyFilter())
    detectWithFilter(getTriangleFilter())
    detectWithFilter(getCircleFilter())

