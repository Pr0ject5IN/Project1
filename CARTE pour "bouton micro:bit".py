from microbit import *

while True:
    if button_a.is_pressed():
        uart.write('A')
        sleep(200)  
    elif button_b.is_pressed():
        uart.write('B')
        sleep(200) 
    elif accelerometer.was_gesture('down'):
        uart.write('logo')
        sleep(200)
