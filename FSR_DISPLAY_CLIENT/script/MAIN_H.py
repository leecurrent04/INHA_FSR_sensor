from .config import *

import numpy as np
import cv2


def makeImg(fsr_matrix):
	img = np.zeros(
        shape=(
            SENSOR_Y_MAX*IMG_PIXEL_SIZE,
            SENSOR_X_MAX*IMG_PIXEL_SIZE 
            ),
        dtype=np.uint8
        )
	
	for y in range(SENSOR_Y_MAX):
		for x in range(SENSOR_X_MAX):
			color = fsr_matrix[x][y]*0.415
			#color = 255 if fsr_matrix[x][y]>255 else fsr_matrix[x][y]

			cv2.rectangle(img, 
						  (x*IMG_PIXEL_SIZE,y*IMG_PIXEL_SIZE),
						  ((x+1)*IMG_PIXEL_SIZE, (y+1)*IMG_PIXEL_SIZE),
						  int(color),		# SENSOR DATA
						  -1
						  )

	return img