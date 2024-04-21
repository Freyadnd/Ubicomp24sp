import time
import board
import busio
import adafruit_tcs34725

# initiateI2C
i2c = busio.I2C(board.SCL, board.SDA)
# initiate color picker
sensor = adafruit_tcs34725.TCS34725(i2c)

def get_color():
    # pick color
    color = sensor.color_rgb_bytes
    print("颜色 RGB: {}".format(color))
    return color

while True:
    color = get_color()
    # frequency
    time.sleep(1)
