## Circuit Playground Kettlebell Exercise Counter Bracelet Documentation

This documentation outlines the setup and use of a wearable exercise counter bracelet designed with the Adafruit Circuit Playground. The bracelet is intended to help fitness enthusiasts track their kettlebell exercises by counting repetitions and sets, providing auditory feedback upon completion of each set, and alerting the user with a different tone when a repetition is performed with proper form.

### Overview

The Circuit Playground Kettlebell Exercise Counter Bracelet is an innovative wearable device that enhances workout sessions by ensuring exercises are done effectively and consistently. It uses the built-in accelerometer to detect the motion of kettlebell lifts, counts them, and provides feedback through sounds.

### Components Needed

- **Adafruit Circuit Playground**: Either Classic or Express model.
- **Wearable Housing**: Fabric wristband or a 3D-printed bracelet to mount the Circuit Playground.
- **USB Cable**: For programming the Circuit Playground.
- **Portable Power Source**: Such as a rechargeable lithium-polymer battery.
- **Optional**: Additional speaker for louder feedback tones.

### Setup and Installation

#### Hardware Setup

1. **Mount the Circuit Playground onto the wristband** or bracelet. Ensure that it is secure and the sensors are unobstructed.
2. **Connect the power source**. If using a rechargeable battery, make sure it is fully charged before starting your workout.

#### Software Setup

1. **Install the Arduino IDE**: Download and install from the [Arduino website](https://www.arduino.cc/en/software).
2. **Set up the Adafruit Circuit Playground library**:
   - Open Arduino IDE.
   - Go to **Sketch > Include Library > Manage Libraries**.
   - Search for **Adafruit Circuit Playground** and install the library.

### Programming

Here’s a simple script to start with. It initializes the device, uses the accelerometer to detect when the kettlebell is lifted (a simple threshold-based detection), and counts the repetitions and sets.

#### Basic Exercise Counter Code

```cpp
#include <Adafruit_CircuitPlayground.h>

int repCount = 0;
int setCount = 0;
const int repsPerSet = 10; // Number of reps per set
const int totalSets = 3;   // Total sets to complete
bool inRep = false;

void setup() {
  CircuitPlayground.begin();
  CircuitPlayground.playTone(440, 500);  // Start-up tone
}

void loop() {
  // Detect kettlebell lift
  if (CircuitPlayground.motionZ() > 10 && !inRep) {
    inRep = true;
    repCount++;
    CircuitPlayground.playTone(880, 100); // Tone for good rep
  } else if (CircuitPlayground.motionZ() <= 10 && inRep) {
    inRep = false;
  }

  // Check if set is complete
  if (repCount >= repsPerSet) {
    setCount++;
    repCount = 0;
    CircuitPlayground.playTone(440, 1000); // Tone for set completion

    if (setCount >= totalSets) {
      CircuitPlayground.playTone(660, 1500); // Workout completion tone
      setCount = 0; // Reset for new session
    }
  }
  delay(50);
}
```

### Usage Instructions

1. **Wear the bracelet on your wrist** securely before starting your exercise.
2. **Power on the Circuit Playground**.
3. **Perform your kettlebell exercises**. The device will automatically count each repetition and set.
4. **Listen for tones**: A short high-pitched tone indicates a good repetition, and a longer tone signifies the completion of a set. A different high-pitched long tone indicates the completion of all sets.

### Safety and Maintenance

- Ensure the device is secured properly to prevent it from flying off during vigorous activities.
- Keep the device dry and clean. Wipe down after workouts if necessary.
- Charge the battery regularly and store in a cool, dry place.

### Troubleshooting

- **Device does not count reps**: Ensure movements are not too gentle. Adjust the threshold in the code if necessary.
- **Inaccurate rep counting**: Refine motion detection logic to better suit your exercise style.
- **No sound or weak sound**: Check the battery and ensure the speaker is not obstructed.

### Conclusion

The Circuit Playground Kettlebell Exercise Counter Bracelet is a valuable tool for fitness enthusiasts who wish to track their kettlebell exercise regimen accurately. By following the setup and usage guidelines provided, users can enhance their fitness routines and ensure that they are performing their exercises effectively and consistently.