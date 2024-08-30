import cv2
import numpy as np

from script.config import *
from script.MAIN_H import *
from script import socket

sc = socket.SocketTel()

while cv2.waitKey(33) != ord('q'):
	sc.send("0,1,2")

	fsr1 = sc.receive()
	fsr2 = sc.receive()
	fsr3 = sc.receive()
	fsr = fsr1[:-1]+","+fsr2[:-1]+","+fsr3

	fsr_value = np.fromstring(
			fsr,
			dtype=np.uint16,
			sep=','
			).reshape(SENSOR_Y_MAX,SENSOR_X_MAX)

	fsr_value = np.transpose(fsr_value)

	makeImg(fsr_value)
	cv2.imshow('img', img)

sc.send("CLOSE")
sc.close()
cv2.destroyAllWindows()
