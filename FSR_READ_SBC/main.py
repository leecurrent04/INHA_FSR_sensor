import socket
import numpy as np
import ctypes

from config import *

fsr = ctypes.cdll.LoadLibrary("./libfsr.so")
fsr.init();
fsr.on();

# create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SOCKET_HOST, SOCKET_PORT))
server_socket.listen(5)

print(f"{SOCKET_HOST}:{SOCKET_PORT} waiting...")

fsr.getData.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int * 8 * 8)]
value = np.zeros(
        shape=(SENSOR_X_MAX, SENSOR_Y_MAX),
        dtype=np.uint8
        )
arr_ctypes = value.ctypes.data_as(ctypes.POINTER(ctypes.c_int * 8 * 8))


while 1:
    # waiting for client
    client_socket, client_address = server_socket.accept()
    print(f"{client_address} is connected.")
   
    while 1:
        try:
            # get data from client
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                continue

            if data == "CLOSE":
                client_socket.close()
                exit(0);

            print(f"client: {data}")

            fsr.getData(0,arr_ctypes)

            # send data to client
            response = f"{value}"
            client_socket.send(response.encode("utf-8"))

        except Exception as e:
            print(f"ERR: {e}")

