from .config import *
import socket
import numpy as np

class SocketTel:
	def	__init__(self, ip=SOCKET_ADDRESS, port=SOCKET_PORT):

		# 서버에 연결
		print(ip)
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client_socket.connect((ip, port))

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

	def getFsr(self, fsr_list, x_max=SENSOR_X_MAX, y_max=SENSOR_Y_MAX):
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
				).reshape(y_max,x_max)

		return fsr_value



