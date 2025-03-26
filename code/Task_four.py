from machine import Pin, I2C
import time

temp_sensor = I2C(scl=Pin(22), sda=Pin(23))

address = 24
temp_reg = 5
res_reg = 8  # Unused in this example, but kept per your original code

leds = [
    Pin(27, Pin.OUT),  # green_led
    Pin(12, Pin.OUT),  # blue
    Pin(13, Pin.OUT),  # red_led
]

currently_on_index = 0

def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp

while True:
    data = temp_sensor.readfrom_mem(address, temp_reg, 2)
    temperature = temp_c(data)
    print("Current Temperature: {:.2f}°C".format(temperature))
    time.sleep(0.1)

    if temperature < 25:
        leds[0].value(0)
        leds[1].value(1)
        leds[2].value(1)
    elif temperature < 27:
        leds[0].value(0)
        leds[1].value(1)
        leds[2].value(0)
    else:
        leds[0].value(1)
        leds[1].value(1)
        leds[2].value(0)
