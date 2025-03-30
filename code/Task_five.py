from machine import Pin, ADC, PWM
import time


duty_local = 1000

green_led = PWM(Pin(27), freq=100000, duty=duty_local)  # green_led
blue_led =  PWM(Pin(12), freq=100000, duty=duty_local)  # blue
red_led =  PWM(Pin(13), freq=100000, duty=duty_local)  # red_led
adc1 = ADC(Pin(34))
adc1.atten(ADC.ATTN_11DB)

min_reading = 142000
max_reading = 3139000
increment = (max_reading-min_reading)/1023

while True:
    print(adc1.read_uv())
    value  = adc1.read_uv()
    duty_local = int((value - min_reading) / increment)
    green_led.duty(duty_local)
    blue_led.duty(duty_local)
    red_led.duty(duty_local)
    print(f"Current duty {duty_local}")

