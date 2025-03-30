from machine import Pin

leds = [
    Pin(13,Pin.OUT), #green_led
    Pin(12,Pin.OUT), #yellow_led
    Pin(27,Pin.OUT), #red_led
]

button = Pin(34, Pin.IN, Pin.PULL_UP)

# A variable which follows which LED is currently on
current_on_index = 0 

# Start with the green light on
leds[0].value(1)

        
while True:
    print(f"Button value: {button.value()}")
    # If button is pressed its value will be equal to 1 (which is equivalent to True)
    if button.value():
        leds[current_on_index].value(0)
        # ill use the remainder function to handle the index going over 2
        current_on_index = (current_on_index + 1) % 3
        leds[current_on_index].value(1)
        # Use the loop to handle when user is holding down the button
        while button.value():
            pass
        # Accept a new input change of LED only after the button has been released and pressed again
        