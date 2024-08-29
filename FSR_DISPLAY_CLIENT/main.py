import cv2
import numpy as np

from script.config import *
from script.MAIN_H import *
from script import socket

sc = socket.SocketTel()

while cv2.waitKey(33) != ord('q'):
	sc.send("0")

	fsr_value = np.fromstring(
			sc.receive(),
			dtype=np.uint16,
			sep=','
			).reshape(8,8)

	makeImg(fsr_value)
	cv2.imshow('img', img)

sc.send("CLOSE")
sc.close()
cv2.destroyAllWindows()
