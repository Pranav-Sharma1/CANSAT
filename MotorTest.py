from machine import Pin, PWM
from utime import sleep

in2 = PWM(Pin(2))     # Speed
in1 = Pin(1, Pin.OUT)  # Direction

in2.freq(500)         # set frequency. 1000 is default

while True:
    # Forward
    # in2:  1023 <-- Slower - Faster --> 0
    in1.on()
    print("Forward")
    in2.duty(0)  # type: ignore # Fast
    sleep(1)
    in2.duty(100)  # Slow # type: ignore
    sleep(1)
    in2.duty(200)  # Slower # type: ignore
    sleep(1)
    in2.duty(300)  # Slower x 2 # type: ignore
    sleep(1) 
    in2.duty(1023)  # stop # type: ignore
    sleep(1)

    # Reverse
    # in2:  0 <-- Slower - Faster --> 1023
    in1.off()
    print("Reverse")    
    in2.duty(900)  # Fast # type: ignore
    sleep(1)
    in2.duty(600)    # Slow # type: ignore
    sleep(1)
    in2.duty(300)    # Slower # type: ignore
    sleep(1)
    in2.duty(0)     # Stopped# type: ignore
    sleep(1)