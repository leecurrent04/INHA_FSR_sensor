from .config import *
import socket
import numpy as np

class SocketTel:
	def	__init__(self):

		# 서버에 연결
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client_socket.connect((SOCKET_ADDRESS, SOCKET_PORT))

	def send(self, message):
		request = f"{message}"
		self.client_socket.send(request.encode("utf-8"))

	def receive(self):
		response = self.client_socket.recv(1024).decode("utf-8")
		return response

	def close(self):
		self.client_socket.close()

	def requestFsr(self, fsr_list):
		msg=""
		for index in fsr_list:
			msg+=f"{index},"	

		msg = msg[:-1]
		self.send(msg)

	def getFsr(self, fsr_list):
		# get data and merge (str)
		values=""
		for value in fsr_list:
			values += self.receive()[:-1] + ","

		values = values[:-1]

		# str convert to np.array
		fsr_value = np.fromstring(
				values,
				dtype=np.uint16,
				sep=','
				).reshape(SENSOR_Y_MAX,SENSOR_X_MAX)

		return fsr_value



