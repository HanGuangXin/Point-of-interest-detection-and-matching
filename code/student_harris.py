import cv2
import numpy as np
import math
import time

def ANMS (x, y, r, maximum):        # Adaptive non-maximum suppression
    '''
    param:
        -> x: is an array of length N
        -> y: is an array of length N
        -> r: is the cornerness score
        -> maximum: is the number of corners that are required
    '''
    time_start = time.time()
    i = 0
    j = 0
    NewList = []
    while i < len(x):
        minimum = 1000000000000         # random large value
        FirstCoordinate, SecondCoordinate = x[i], y[i]
        while j < len(x):
            CompareCoordinate1, CompareCoordinate2 = x[j], y[j]
            if (FirstCoordinate != CompareCoordinate1 and SecondCoordinate != CompareCoordinate2) and r[i] < r[j]:
                distance = math.sqrt((CompareCoordinate1 - FirstCoordinate)**2 + (CompareCoordinate2 - SecondCoordinate)**2)
                if distance < minimum:
                    minimum = distance
            j = j + 1
        NewList.append([FirstCoordinate, SecondCoordinate, minimum])
        i = i + 1
        j = 0
    NewList.sort(key=lambda t: t[2])
    NewList = NewList[len(NewList)-maximum:len(NewList)]

    time_end = time.time()
    print('ANMS cost:', time_end - time_start)
    return NewList


def get_interest_points(image, feature_num):
    time_start = time.time()
    alpha = 0.06            # parameter to calculate corner function R
    threshold = 12000        # threshold to determine corners
    XCorners = []
    YCorners = []
    RValues = []
    # Compute the size of the image.
    ImageRows = image.shape[0]
    ImageColumns = image.shape[1]
    # Use the Soble filter to calculate the x and y derivative of the image
    Xderivative = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    Yderivative = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    # Define matrices Ixx, Iyy and Ixy
    Ixx = Xderivative * Xderivative
    Iyy = Yderivative * Yderivative
    Ixy = Xderivative * Yderivative
    # loop over the image to compute cornerness score of each pixel
    for i in range(16, ImageRows - 16):         # the region that can generate cell 16×16
        for j in range(16, ImageColumns - 16):      # the region that can generate cell 16×16
            Ixx1 = Ixx[i-1:i+1, j-1:j+1]
            Iyy1 = Iyy[i-1:i+1, j-1:j+1]
            Ixy1 = Ixy[i-1:i+1, j-1:j+1]
            Ixxsum = Ixx1.sum()
            Iyysum = Iyy1.sum()
            Ixysum = Ixy1.sum()
            Determinant = Ixxsum*Iyysum - Ixysum**2     # Calculate the eigenvalues of the matrix
            Trace = Ixxsum + Iyysum                     # Matrix trace
            R = Determinant - alpha*(Trace**2)          # Corner function R
            # Check if the cornerness score is above the threshold and if the pixel is an eligible corner pixel
            if R > threshold:
                XCorners.append(j)
                YCorners.append(i)
                RValues.append(R)
    XCorners = np.asarray(XCorners)
    YCorners = np.asarray(YCorners)
    RValues = np.asarray(RValues)
    # Use ANMS to evenly distribute the corners in the image.
    # NewCorners = noANMS(XCorners, YCorners)
    NewCorners = ANMS(XCorners, YCorners, RValues, feature_num)     # Adaptive non-maximum suppression
    NewCorners = np.asarray(NewCorners)
    print('before ANMS ' + 'img' + 'has corners num:'+str(len(XCorners)))
    print('after ANMS ' + 'img' + 'has corners num:'+str(len(NewCorners)))
    # Return the x-y coordinates and cornerness score of the eligible corners.
    x = NewCorners[:, 0]
    y = NewCorners[:, 1]

    time_end = time.time()
    print('get_interest_points cost:', time_end - time_start)
    return x, y, RValues


