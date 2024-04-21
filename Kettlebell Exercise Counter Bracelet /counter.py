from adafruit_circuitplayground import cp
import time

# set parameter
sets = 3  
reps_per_set = 10  
threshold = 15  

# initiate
reps_done = 0
sets_done = 0

while sets_done < sets:
    cp.red_led = True  # start point
    while reps_done < reps_per_set:
        # accelerator
        x, y, z = cp.acceleration
        if abs(z) > threshold:
            # detect action
            reps_done += 1
            print(f"Rep {reps_done} done")
            cp.play_tone(440, 0.1)  # play sound
            time.sleep(1)  # avoid multi-count
    cp.play_tone(262, 1)  # different sound
    print(f"Set {sets_done + 1} completed")
    reps_done = 0
    sets_done += 1
    cp.red_led = False
    time.sleep(3)  # rest

print("Workout completed!")
cp.play_tone(523, 2)  # final sound
