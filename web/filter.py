import cv2
def Filter(img, function, kernel):
    if function == "average":
        return cv2.blur(img, (kernel, kernel))
    elif function == "median":
        return cv2.medianBlur(img, kernel)
    elif function == "gaussian":
        return cv2.GaussianBlur(img, (kernel, kernel), 0)
    elif function == 'sobelx':
        return cv2.Sobel(img,cv2.CV_64F,1,0,ksize=kernel)
    elif function == 'sobely':
        return cv2.Sobel(img,cv2.CV_64F,0,1,ksize=kernel)
    elif function == 'laplacian':
        return cv2.Laplacian(img, cv2.CV_64F)



