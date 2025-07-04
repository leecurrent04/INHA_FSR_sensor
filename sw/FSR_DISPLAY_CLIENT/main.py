import cv2
import numpy as np

import tensorflow as tf
from tensorflow import keras

from script.config import *
from script import socket
from script import displayImg as dp
from script.filter import *

model = tf.keras.models.load_model("./img/my_model.keras")
class_names = ['BOTH', 'Four', 'LEFT', 'LLR', 'LRR', 'RIGHT']


sc = socket.SocketTel()
sc2 = socket.SocketTel("192.168.0.5", 12346)

while cv2.waitKey(33) != ord('q'):
	# request fsr data
	sc.requestFsr(SELECTED_FSR)
	sc2.requestFsr([3])

	# get fsr data
	fsr_value = sc.getFsr(SELECTED_FSR)
	fsr_value = np.transpose(fsr_value)

	fsr_value_hand = sc2.getFsr([3], 8, 8)
	fsr_value_hand = np.transpose(fsr_value_hand)
	
	#저주파 통과 필터 적용
	fsr_value_filter = setLPFilter(fsr_value, 0.3) 
	
	img_original = dp.makeImg(fsr_value)
	img_LPF = dp.makeImg(fsr_value_filter)

	img_hand = dp.makeImg(fsr_value_hand, 8,8)

	cv2.imshow('img', img_original)
	cv2.imshow('LPF', img_LPF)

	cv2.imshow('HAND', img_hand)

	if np.amax(img_original) < 100:
		print("NONE")
	else:
		img_array = tf.keras.utils.img_to_array(np.transpose(fsr_value))
		img_array = tf.expand_dims(img_array, 0) # Create a batch

		predictions = model.predict(img_array)
		score = tf.nn.softmax(predictions[0])

		print(
			"%02.2f %02.2f"%(
				score[class_names.index("LEFT")]+score[class_names.index("RIGHT")]+score[class_names.index("BOTH")],
				score[class_names.index("LRR")]+score[class_names.index("LLR")]+score[class_names.index("Four")]
				)
			)
		#print(
			#"This image most likely belongs to {} with a {:.2f} percent confidence."
			#.format(class_names[np.argmax(score)], 100 * np.max(score))
		#)


	#print(np.max(fsr_value))

sc.send("CLOSE")
sc.close()
sc2.send("CLOSE")
sc2.close()
cv2.destroyAllWindows()
