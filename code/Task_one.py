from machine import Pin
import time

p=Pin(13,Pin.OUT)


while True:
    p.value(1)
    print("on")
    time.sleep(0.5)
    p.value(0)
    print("off")
    time.sleep(0.5)