from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time, math

options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.chain_length = 2
options.hardware_mapping = 'adafruit-hat'
options.gpio_slowdown = 4

matrix = RGBMatrix(options=options)

size = 15
cx, cy = 32, 16

shape = [(x, y)
         for x in range(cx - size//2, cx + size//2)
         for y in range(cy - size//2, cy + size//2)]

def draw(points):
    matrix.Clear()
    for x, y in points:
        if 0 <= x < 64 and 0 <= y < 32:
            matrix.SetPixel(x, y, 0, 255, 0)
    time.sleep(0.05)

while True:
    for angle in range(0, 360, 4):
        rad = math.radians(angle)
        cosA, sinA = math.cos(rad), math.sin(rad)

        rotated = []
        for x, y in shape:
            xt, yt = x - cx, y - cy
            xr = xt * cosA - yt * sinA
            yr = xt * sinA + yt * cosA
            rotated.append((round(xr + cx), round(yr + cy)))

        draw(rotated)