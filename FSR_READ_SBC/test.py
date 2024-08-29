import ctypes
import numpy as np

# FSR
fsr = ctypes.cdll.LoadLibrary("./libfsr.so")
fsr.init();
fsr.on();

fsr.getData.argtypes = [ctypes.c_uint8, ctypes.POINTER(ctypes.c_uint16 * 8 * 8)]
value = np.zeros(
        shape=(8, 8),
        dtype=np.uint16
        )
arr_ctypes = value.ctypes.data_as(ctypes.POINTER(ctypes.c_uint16 * 8 * 8))

while 1:
    text=""

    print(fsr.getData(0, arr_ctypes))

    for y in range(8):
        for x in range(8):
            text+=f"{value[x][y]},"
        text = f"{text[:-1]}\n"

    print(text)


