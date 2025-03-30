from machine import Pin, I2C
import time

# This tasks code follows the same idea as for task three, but in this case we have the LED pins routed to a RGB led

temp_sensor = I2C(scl=Pin(22), sda=Pin(23))

address = 24
temp_reg = 5

# After some testing we concluded that we have a common-anode type LED
# Meaning that we have connected it to VCC rather than GND and from a coding perspective the values are inverted:
# a pin with value of 1 means that specific led "color" is off and with the value of 0 it's on
leds = [
    Pin(27, Pin.OUT),  # green_led
    Pin(12, Pin.OUT),  # blue_led
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
        # Set only green light on
        leds[0].value(0)
        leds[1].value(1)
        leds[2].value(1)
    elif temperature < 27:
        # Set green + red = yellow light on
        leds[0].value(0)
        leds[1].value(1)
        leds[2].value(0)
    else:
        # set red light on
        leds[0].value(1)
        leds[1].value(1)
        leds[2].value(0)
