
from machine import Pin
from machine import I2C
from bmp280 import BMP280
import time

global pressure
global temp
global altitude

i2c_bus = I2C(1, sda=Pin(6), scl=Pin(7))
bmp = BMP280(i2c_bus)

pressure = bmp.getPress()
temp = bmp.getTemp()
altitude = bmp.getAlti()
while True:
# The following lines of code should be tested in the REPL:
# 1. To get envirment temperature (^C):
    print(temp)
#
# 2. To get Pressure (hPa):
    print(pressure)
#
# 3. To calculate absolute altitude (m):
    print(altitude, "\n")

    time.sleep(1)