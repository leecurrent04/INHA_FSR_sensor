import cv2
import numpy as np

from script.config import *
from script.MAIN_H import *
from script import socket
from script.filter import setMAFilter
from script.filter import setLPFilter

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
	fsr_value_filter = setLPFilter(fsr_value,0.25) 
	
	img_original = makeImg(fsr_value)
	img_LPF = makeImg(fsr_value_filter)
	
	cv2.imshow('img', img_original)
	cv2.imshow('img_filter', img_LPF)
	#cv2.imshow('img diff', img_original-img_LPF)

	#print(np.max(fsr_value))

sc.send("CLOSE")
sc.close()
cv2.destroyAllWindows()
