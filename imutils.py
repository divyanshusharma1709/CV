import cv2
import numpy as np

def translate(image, x, y):
	M = np.float32([[1, 0, x], [0, 1, y]])
	rows, cols, ch = image.shape
	dst = cv2.warpAffine(image,M,(cols, rows))
	return dst

