import cv2
import numpy as np

from script.config import *
from script import socket
from script import displayImg as dp
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
	
	img_original = dp.makeImg(fsr_value)
	img_LPF = dp.makeImg(fsr_value_filter)

	cv2.imshow('img', img_original)
	cv2.imshow('LPF', img_LPF)

	#print(np.max(fsr_value))

sc.send("CLOSE")
sc.close()
cv2.destroyAllWindows()
