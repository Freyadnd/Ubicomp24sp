from adafruit_circuitplayground import cp
import time

sounds = {
    'A1': 'hi-hat',
    'A2': 'snare-drum',
    'A3': 'bass-drum',
    'A4': 'cymbal',
    'A5': 'tom-tom'
}

loop_active = False  # Controls the loop playback state

# Function to play sounds
def play_sound(sound):
    if sound == "hi-hat":
        cp.play_tone(4000, 0.1)  # Hi-hat
    elif sound == "snare-drum":
        cp.play_tone(200, 0.3)  # Snare drum
    elif sound == "bass-drum":
        cp.play_tone(60, 0.5)  # Bass drum
    elif sound == "cymbal":
        cp.play_tone(3200, 0.2)  # Cymbal
    elif sound == "tom-tom":
        cp.play_tone(160, 0.4)  # Tom-tom

all_events = []  # Stores all recorded sound events

def check_and_play_events():
    current_time = time.monotonic()
    for event in list(all_events):  # Create a list copy to allow modifications
        event_time, sound = event
        if current_time >= event_time:
            play_sound(sound)
            all_events.remove(event)  # Remove played event
            all_events.append((current_time + 6, sound))  # Reschedule event to play after 6 seconds

def update_leds(loop_status):
    # Update LED based on loop status
    if loop_status:
        # Light up the first LED with a soft green light to indicate looping is active
        cp.pixels[0] = (0, 20, 0)  # Soft green color
    else:
        # Turn off the first LED
        cp.pixels[0] = (0, 0, 0)

# Main loop
while True:
    # Check each touch pad and play the associated sound
    for touch_pad, sound in sounds.items():
        if getattr(cp, f'touch_{touch_pad}'):
            play_sound(sound)
            if loop_active:
                next_play_time = time.monotonic() + 6  # Schedule to play after 6 seconds
                all_events.append((next_play_time, sound))

    if cp.button_b:
        loop_active = not loop_active  # Toggle loop playback state
        update_leds(loop_active)  # Update LED indicator based on loop state
        if loop_active:
            print("Loop started")
        else:
            print("Loop stopped")
            all_events.clear()  # Clear all events when loop is stopped

    if loop_active:
        check_and_play_events()  # Check and play sound events

    time.sleep(0.01)  # Short delay to reduce CPU load
