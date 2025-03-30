from machine import Pin, I2C
import time

temp_sensor = I2C(scl=Pin(22), sda=Pin(23))

# Before this we used temp_sensor.scan() function to check for available adresses and chose one
address = 24
temp_reg = 5

leds = [
    Pin(27, Pin.OUT),  # green_led
    Pin(12, Pin.OUT),  # yellow_led
    Pin(13, Pin.OUT),  # red_led
]
# Variable follows the same idea as in task two
currently_on_index = 0

# A function that returns the signed 12-bit temperature value in Celsius
def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp

while True:
    # calls the integrated function that reads 2 bytes from the device address and returns a byte string
    data = temp_sensor.readfrom_mem(address, temp_reg, 2)
    #take the temperature from the byte string
    temperature = temp_c(data)
    print("Current Temperature: {:.2f}°C".format(temperature))
    time.sleep(0.1)

    if temperature < 25:
        #Turn off previous LED and turn on green LED
        leds[currently_on_index].value(0)
        currently_on_index = 0
        leds[currently_on_index].value(1)
    elif temperature < 28:
        #Turn off previous LED and turn on yellow LED
        leds[currently_on_index].value(0)
        currently_on_index = 1
        leds[currently_on_index].value(1)
    else:
        #Turn off previous LED and turn on red LED
        leds[currently_on_index].value(0)
        currently_on_index = 2
        leds[currently_on_index].value(1)
    
