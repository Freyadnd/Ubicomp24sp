import board
import time
import math
from adafruit_circuitplayground import cp
import analogio
import simpleio

# Initialize joystick
joystick_x = analogio.AnalogIn(board.A1)  # X axis
joystick_y = analogio.AnalogIn(board.A2)  # Y axis

# Function to read joystick value
def get_joystick_angle():
    x = simpleio.map_range(joystick_x.value, 0, 65535, -1, 1)
    y = simpleio.map_range(joystick_y.value, 0, 65535, -1, 1)
    angle = (math.atan2(y, x) * 180.0 / math.pi) + 180  # Convert to 0-360 degrees
    return angle

# Color wheel in RGB
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 128, 0), (0, 255, 255), (0, 0, 255), (75, 0, 130), (238, 130, 238), (255, 0, 0)]

# Setup number display (implement based on your display's library)
def display_number(number):
    print("Time: {} minutes".format(number))  # Placeholder for actual display function

# Work time calculation
def calculate_work_time(angle):
    if angle < 90:  # Red to Yellow
        return 50  # More energetic, longer work time
    elif angle < 270:  # Yellow to Blue
        return 25  # Less energetic, shorter work time
    else:
        return 50  # Back to energetic

# Main loop
while True:
    cp.pixels.fill((0, 0, 0))  # Turn off all LEDs
    angle = get_joystick_angle()
    index = int(angle / 36)  # There are 10 sections, each 36 degrees
    cp.pixels[index] = colors[index]  # Light up the selected LED

    if cp.button_a:  # Assume button A is used to select the color/work period
        work_time = calculate_work_time(angle)
        display_number(work_time)
        # Start countdown (implement countdown logic)
        for i in range(work_time * 60, -1, -1):  # Countdown in seconds
            minutes = i // 60
            seconds = i % 60
            display_number(minutes)  # Update number display each minute
            time.sleep(1)

    time.sleep(0.1)  # Small delay to debounce inputs and reduce CPU usage
