from .config import *
import socket

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
		# print(f"서버 : {response}\n")

	def close(self):
		self.client_socket.close()
