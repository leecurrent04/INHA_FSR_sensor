from .config import *

import numpy as np
import cv2


def makeImg(fsr_matrix,x_max=SENSOR_X_MAX,y_max=SENSOR_Y_MAX):
	img = np.zeros(
        shape=(
            y_max*IMG_PIXEL_SIZE,
            x_max*IMG_PIXEL_SIZE 
            ),
        dtype=np.uint8
        )
	
	for y in range(y_max):
		for x in range(x_max):
			color = fsr_matrix[x][y] * IMG_RANGE_ADJUSTMENT_FACTOR
			color = 255 if color>255 else color

			cv2.rectangle(img, 
						  (x*IMG_PIXEL_SIZE,y*IMG_PIXEL_SIZE),
						  ((x+1)*IMG_PIXEL_SIZE, (y+1)*IMG_PIXEL_SIZE),
						  int(color),		# SENSOR DATA
						  -1
						  )

	return img