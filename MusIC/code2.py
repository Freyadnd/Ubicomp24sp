from adafruit_circuitplayground import cp
import time

WORK_TIME = 25 * 60  # 25 minutes
SHORT_BREAK = 5 * 60  # 5 minutes
LONG_BREAK = 15 * 60  # 15 minutes

timer = WORK_TIME
state = 'work'
is_running = False

def update_leds():
    total_time = WORK_TIME if state == 'work' else SHORT_BREAK if state == 'short_break' else LONG_BREAK
    leds_on = round((timer / total_time) * 10)  # calculate the number of LEDs to light
    for i in range(10):
        if i < leds_on:
            cp.pixels[i] = (0, 255, 0) if state == 'work' else (0, 0, 255)
        else:
            cp.pixels[i] = (0, 0, 0)

while True:
    if cp.button_a:  # toggle running state
        is_running = not is_running
        while cp.button_a:  # debounce button A
            pass
        if is_running:
            print("Timer started")
        else:
            print("Timer paused")
    
    if cp.button_b:  # reset the timer
        timer = WORK_TIME
        state = 'work'
        is_running = False
        print("Timer reset")
        while cp.button_b:  # debounce button B
            pass
    
    if is_running:
        if timer > 0:
            update_leds()
            time.sleep(1)
            timer -= 1
        else:
            if state == 'work':
                state = 'short_break' if (timer // WORK_TIME) % 8 != 0 else 'long_break'
                timer = SHORT_BREAK if state == 'short_break' else LONG_BREAK
                cp.play_tone(500, 1)  # signal break start
            else:
                state = 'work'
                timer = WORK_TIME
                cp.play_tone(1000, 1)  # signal work start
            print(f"Switched to {state}")
    update_leds()
