import cv2
import numpy as np

def Fourier(img):
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    spectrum = cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])
    log_spectrum = 20*np.log1p(spectrum)
    return log_spectrum


