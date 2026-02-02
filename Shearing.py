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
cx, cy = 20, 8

while True:
    for k in [i/20 for i in range(-10, 11)]:
        matrix.Clear()
        for x, y in shape:
            xs = round(x + k * y + cx)
            ys = y + cy
            if 0 <= xs < 64 and 0 <= ys < 32:
                matrix.SetPixel(xs, ys, 255, 255, 0)
        time.sleep(0.08)