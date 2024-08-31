import cv2
import numpy as np 


from script import socket
from script.config import *
from script.displayImg import *
from script.filter import *

sc = socket.SocketTel()

while cv2.waitKey(33) != ord('q'):
	# request fsr data
	sc.requestFsr(SELECTED_FSR)

	# get fsr data
	fsr_value = sc.getFsr(SELECTED_FSR)
	fsr_value = np.transpose(fsr_value)
	
	#저주파 통과 필터 적용
	fsr_value_filter = setLPFilter(fsr_value, 0.3) 
	
	img_original = makeImg(fsr_value)
	img_LPF = makeImg(fsr_value_filter)
	
	img_bilateral = cv2.bilateralFilter(img_original, -1, 10, 5)

	cv2.imshow('img', img_original)
	cv2.imshow('LPF', img_LPF)
	cv2.imshow('Gaussian', img_bilateral)

	print(np.max(fsr_value))

sc.send("CLOSE")
sc.close()
cv2.destroyAllWindows()
