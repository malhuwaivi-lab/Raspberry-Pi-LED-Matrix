from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time

options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.chain_length = 2
options.hardware_mapping = 'adafruit-hat'
options.gpio_slowdown = 4

matrix = RGBMatrix(options=options)

size = 15
shape = [(x, y) for x in range(size) for y in range(size)]

while True:
    for dx in range(0, 64 - size):
        matrix.Clear()
        for x, y in shape:
            matrix.SetPixel(x + dx, y + 8, 255, 0, 0)
        time.sleep(0.05)