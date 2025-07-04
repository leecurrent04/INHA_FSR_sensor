import socket
import numpy as np
import ctypes

from config import *

# create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SOCKET_HOST, SOCKET_PORT))
server_socket.listen(5)

print(f"{SOCKET_HOST}:{SOCKET_PORT} waiting...")

# FSR
fsr = ctypes.cdll.LoadLibrary("./libfsr.so")
fsr.init();
fsr.on();

fsr.getData.argtypes = [
        ctypes.c_uint8,
        ctypes.POINTER(ctypes.c_uint16 * SENSOR_X_MAX * SENSOR_Y_MAX)
        ]
value = np.zeros(
        shape=(SENSOR_X_MAX, SENSOR_Y_MAX),
        dtype=np.uint16
        )
arr_ctypes = value.ctypes.data_as(
        ctypes.POINTER(ctypes.c_uint16 * SENSOR_X_MAX * SENSOR_Y_MAX)
        )

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

            # print(f"client: {data}")
            part = data.split(",")
            for i in part:

                fsr.getData(int(i),arr_ctypes)

                # send data to client
                response=""
                for y in range(8):
                    for x in range(8):
                        response+=f"{value[x][y]},"
                response = f"{response[:-1]}\n"
                
                #response = f"{value}"
                client_socket.send(response.encode("utf-8"))

        except Exception as e:
            print(f"ERR: {e}")

