from machine import pin, ADC, PWM
import time
while True:
    heat_detected = 0
    heat_start_time = 0
    timer_active = 0  #if not active 0 if active then 1
    total_timer = 0  #total time left on timer even after stacking
    buzzer = 0
    auto_alarm_limit = 300

    #main program
    heat_sensor = ADC(Pin(26)) 
    timer_button = ADC(Pin(14))
    end_button = ADC(Pin(16))

    buzzer = Pin(20, Pin.out)
    led = Pin(16, Pin.out)

    while True:
        current_time = time.time()
        sensor_reading = heat_sensor.read()
        timer_pressed = timer_button.value() #checks how many times it is pressed

        if sensor_reading > heat_line:   #if the reading is more than 100 degrees it starts a timer for 3 minutes
            heat_detected = 1
            heat_start_time = current_time
        if current_time - heat_start_time >= auto_alarm_limit:   # Once it has been more than 3 minutes the buzzer turns on
            buzzer.value(1)
        else: 
            buzzer(0)
        if timer_pressed:
          if timer_active == 0:
               buzzer
               