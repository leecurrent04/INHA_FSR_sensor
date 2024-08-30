import cv2
import numpy as np

from script import socket
from script.config import *
from script.displayImg import *
from script.filter import *

sc = socket.SocketTel()

while cv2.waitKey(33) != ord('q'):
	# request fsr data
	sc.send("2,1,0")

	# get data
	fsr1 = sc.receive()
	fsr2 = sc.receive()
	fsr3 = sc.receive()
	
	# merge data(type : str)
	fsr = fsr1[:-1]+","+fsr2[:-1]+","+fsr3

	# convert str to array
	fsr_value = np.fromstring(
			fsr,
			dtype=np.uint16,
			sep=','
			).reshape(SENSOR_Y_MAX,SENSOR_X_MAX)

	fsr_value = np.transpose(fsr_value)
	
	#저주파 통과 필터 적용
	fsr_value_filter1 = setLPFilter(fsr_value,0.10) 
	fsr_value_filter2 = setLPFilter(fsr_value,0.30) 
	fsr_value_filter3 = setLPFilter(fsr_value,0.50) 
	fsr_value_filter4 = setLPFilter(fsr_value,0.70) 
	
	img_original = makeImg(fsr_value)
	img_LPF1 = makeImg(fsr_value_filter1)
	img_LPF2 = makeImg(fsr_value_filter2)
	img_LPF3 = makeImg(fsr_value_filter3)
	img_LPF4 = makeImg(fsr_value_filter4)
	
	cv2.imshow('img', img_original)
	cv2.imshow('img_filter 0.1', img_LPF1)
	cv2.imshow('img_filter 0.3', img_LPF2)
	cv2.imshow('img_filter 0.5', img_LPF3)
	cv2.imshow('img_filter 0.7', img_LPF4)

	#print(np.max(fsr_value))

sc.send("CLOSE")
sc.close()
cv2.destroyAllWindows()
