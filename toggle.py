# Use the Pin method from the machine software library
from machine import Pin
import time
# Define the inputs and outputs and assign them to software objects
# First argument is a GPIO pin number, rather than a physical pin number
led1 = Pin(16, Pin.OUT)
led2 = Pin(17, Pin.OUT)
led3 = Pin(20, Pin.OUT)
led4 = Pin(18, Pin.OUT)
pico = Pin("LED", Pin.OUT)
sw1 = Pin(10, Pin.IN, Pin.PULL_DOWN)
sw2 = Pin(11, Pin.IN, Pin.PULL_DOWN)
sw3 = Pin(12, Pin.IN, Pin.PULL_DOWN)
sw4 = Pin(13, Pin.IN, Pin.PULL_DOWN)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)

# default state
led_state=False
new_button_state = sw5.value()

while True:
    # update the button state everytime it goes through the loop
    last_button_state = new_button_state
    new_button_state = sw5.value()
    # I want the moment was off and is now on
    if new_button_state == 1 and last_button_state == 0:
        #toggle led
        led1.toggle()
        time.sleep(0.05) # debounce delay
        print("Hello")


