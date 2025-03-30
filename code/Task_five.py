from machine import Pin, ADC, PWM
import time

# Set an initial value of the PWM duty reading
duty_local = 1000

green_led = PWM(Pin(27), freq=100000, duty=duty_local)  # green_led
blue_led =  PWM(Pin(12), freq=100000, duty=duty_local)  # blue
red_led =  PWM(Pin(13), freq=100000, duty=duty_local)  # red_led

adc1 = ADC(Pin(34))
adc1.atten(ADC.ATTN_11DB)

# After performing some tests with the analog input, we gathered the minimum and maximum values of its input range
min_reading = 142000
max_reading = 3139000
# Take the valid input range and divide it by the acceptable duty range [0,1023]
# Creating an increment that splits the analog input range into 1023 equal parts 
increment = (max_reading - min_reading) / 1023

while True:
    # Read the input value
    value  = adc1.read_uv()
    # Convert it into a applicable duty range
    duty_local = int((value - min_reading) / increment)
    # Update the LED values
    green_led.duty(duty_local)
    blue_led.duty(duty_local)
    red_led.duty(duty_local)
    print(f"Current duty {duty_local}")

