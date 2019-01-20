import cv2
def Thres(img, value):
    if value == -1:
        ret1, th1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        return th1
    else:
        ret2,th2 = cv2.threshold(img,value,255,cv2.THRESH_BINARY)
        return th2