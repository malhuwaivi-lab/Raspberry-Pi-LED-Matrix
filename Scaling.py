from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time

options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.chain_length = 2
options.hardware_mapping = 'adafruit-hat'
options.gpio_slowdown = 4

matrix = RGBMatrix(options=options)

cx, cy = 32, 16
base = [(x, y) for x in range(-7, 8) for y in range(-7, 8)]

while True:
    for scale in [i/10 for i in range(5, 20)]:
        matrix.Clear()
        for x, y in base:
            xs = round(cx + x * scale)
            ys = round(cy + y * scale)
            if 0 <= xs < 64 and 0 <= ys < 32:
                matrix.SetPixel(xs, ys, 0, 0, 255)
        time.sleep(0.08)