import cv2

def dilate(img, kernel_size):
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(kernel_size, kernel_size))
    dilation = cv2.dilate(img,kernel,iterations = 1)
    return dilation

def erode(img, kernel_size):
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(kernel_size, kernel_size))
    erosion = cv2.erode(img,kernel,iterations = 1)
    return erosion


def opening(img, kernel_size):
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(kernel_size, kernel_size))
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return opening

def close(img, kernel_size):
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(kernel_size, kernel_size))
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    return closing