import cv2
import numpy as np
import os

from script.config import *
from script import socket
from script import displayImg as dp
from script.filter import *

sc = socket.SocketTel()

# Save directory
save_num = 0
save_path = "./img/%s"%(
	str(input("INPUT DIRECTORY NAME : "))
	)

if not os.path.isdir(save_path):
	os.mkdir(save_path)

while 1:

	# request fsr data
	sc.requestFsr(SELECTED_FSR)

	# get fsr data
	fsr_value = sc.getFsr(SELECTED_FSR)
	fsr_value = np.transpose(fsr_value)

	# show max value
	#print(np.max(fsr_value))
	
	# adjust 8bit image
	img_original = dp.makeImg(fsr_value)

	cv2.imshow('img', img_original)

	key = cv2.waitKey()
	if key == ord('q'): break
	elif key == ord('r'): continue
	elif key == ord('s'):
		cv2.imwrite("%s/%04d.png"%(save_path, save_num), img_original)
		print("%s Saved"%save_num)
		save_num+=1

sc.send("CLOSE")
sc.close()
cv2.destroyAllWindows()

