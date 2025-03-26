from machine import Pin

leds = [
    Pin(13,Pin.OUT), #green_led
    Pin(12,Pin.OUT), #yellow_led
    Pin(27,Pin.OUT), #red_led
]

button = Pin(34, Pin.IN, Pin.PULL_UP)

current_index = 0

leds[0].value(1)

button_off = True         
while True:
    print(button.value())
    if button.value():
        leds[current_index].value(0)
        current_index = (current_index + 1) % 3
        leds[current_index].value(1)
        while button.value():
            pass
        