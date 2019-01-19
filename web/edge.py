import cv2
import numpy as np

def get_edge(img, function):
    if function == 'canny':
        return canny(img)
    elif function == 'sobel':
        return cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    elif function == 'laplacian':
        return cv2.Laplacian(img, cv2.CV_64F)



def canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	result = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return result
    