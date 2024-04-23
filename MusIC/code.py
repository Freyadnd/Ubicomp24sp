from adafruit_circuitplayground import cp
import time

# hard code sound track
sounds = ['hi-hat', 'snare-drum', 'bass-drum', 'cymbal', 'tom-tom']
current_index = 0
loop_active = False  # Controls the loop playback state

# Function to play sounds
def play_sound(sound):
    if sound == "hi-hat":
        cp.play_tone(4000, 0.1)  # Hi-hat
    elif sound == "snare-drum":
        cp.play_tone(200, 0.3)  # Snare drum
    elif sound == "bass-drum":
        cp.play_tone(60, 0.5)  # Bass drum

all_events = []  # Stores all recorded sound events

def check_and_play_events():
    current_time = time.monotonic()
    for event in list(all_events):  # Create a list copy to allow modifications
        event_time, sound = event
        if current_time >= event_time:
            play_sound(sound)
            all_events.remove(event)  # Remove played event
            all_events.append((current_time + 6, sound))  # Reschedule event to play after 6 seconds

# Main loop
while True:
    if cp.button_a:
        current_index = (current_index + 1) % len(sounds)
        play_sound(sounds[current_index])
        time.sleep(0.5)  # Debounce delay

    if cp.touch_A2:
        play_sound(sounds[current_index])
        if loop_active:
            next_play_time = time.monotonic() + 6  # Schedule to play after 6 seconds
            all_events.append((next_play_time, sounds[current_index]))

    if cp.button_b:
        loop_active = not loop_active  # Toggle loop playback state
        if loop_active:
            print("Loop started")
        else:
            print("Loop stopped")
            all_events.clear()  # Clear all events when loop is stopped

    if loop_active:
        check_and_play_events()  # Check and play sound events

    time.sleep(0.01)  # Short delay to reduce CPU load
