## Overview
This project creates a simple music player for the Circuit Playground board, allowing users to play and record different drum sounds using buttons and a touch sensor. The primary focus of this project is to explore audio playback capabilities and user interaction.


## Implementation Details

1. **Audio Playback Method**:
   After researching the audio playback capabilities of the Circuit Playground, I found that hardcoding audio tones is the primary method available for generating sounds. As a result, the audio output might not be particularly harmonious, as it is limited to predefined frequencies and durations.

2. **Version History**:
   - **Initial Version**: Initially, I used Button A on the Circuit Playground to cycle through different sound types. This simple interface allowed users to manually switch between sounds such as hi-hat, snare-drum, and bass-drum.
   - View the script by navigating to [code.py](./code.py) in the project directory.

   - **Improved Version**: The second version of the software introduces an enhanced user interface, where different touch sensors (A1 to A5) on the device are mapped to specific sounds. This update eliminates the need to cycle through sounds using a button and instead assigns a unique sound to each touch sensor, adding more intuitive control. Additional sounds such as cymbals and tom-toms were also integrated to enrich the audio experience. Moreover, an LED indicator was added to visually signify whether the looping feature is active, using a soft green light on the first LED to minimize eye strain.
   - View the script by navigating to [code2.py](./code2.py) in the project directory.

## Features
### Initial Version
- **Sound Switching**: Use button A to cycle through three preset drum sounds (Hi-Hat, Snare Drum, Bass Drum).
- **Sound Playback**: Use touch sensor A2 to play the currently selected sound.
- **Recording and Playback**: Use button B to start recording music, stop recording, and automatically play back the recorded music.

To operate the device:
- Press Button A to change sound track. 
- Touch sensors A1 to play corresponding sounds.
- Press Button B to toggle the looping feature on or off. 


### Improved Version
- **Multiple Sound Playback**: Users can trigger different sounds by touching specific sensors on the Circuit Playground.
- **Looping Capability**: Sounds can be set to loop every 6 seconds, allowing for continuous playback until the loop is manually toggled off.
- **LED Feedback**: The state of the sound loop is indicated by an LED, providing immediate visual feedback about the system status.

To operate the device:
- Touch sensors A1 to A5 to play corresponding sounds.
- Press Button B to toggle the looping feature on or off. The first LED will light up in green when the loop is active.


### Visuals

- **Initial Version Video Demonstration**: [[Link to the demo video](https://drive.google.com/file/d/1ncrKjRcByigJREtMyB1X0YjKiuNG2gcC/view?usp=sharing)]

- **Improved Version Video Demonstration**: [[Link to the demo video](https://drive.google.com/file/d/1ncrKjRcByigJREtMyB1X0YjKiuNG2gcC/view?usp=sharing)]