#include <Adafruit_CircuitPlayground.h>
from adafruit_circuitplayground import cp
import time

#define WORK_TIME 25 * 60 // 25 minutes
#define SHORT_BREAK 5 * 60 // 5 minutes
#define LONG_BREAK 15 * 60 // 15 minutes

enum TimerState {
  WORK,
  SHORT_BREAK,
  LONG_BREAK
};

int timer = WORK_TIME;
TimerState state = WORK;
bool isRunning = false;

void setup() {
  CircuitPlayground.begin();
  Serial.begin(9600);
  updateLEDs();
}

void loop() {
  handleButtonInputs();
  if (isRunning) {
    decrementTimer();
    updateLEDs();
  }
  delay(1000); // Update every second
}

void handleButtonInputs() {
  if (CircuitPlayground.leftButton()) {
    isRunning = !isRunning; // Toggle start/pause
    Serial.println(isRunning ? "Timer started" : "Timer paused");
  }
  if (CircuitPlayground.rightButton()) {
    resetTimer();
    Serial.println("Timer reset");
  }
}

void decrementTimer() {
  if (timer > 0) {
    timer--;
    Serial.print("Time left: ");
    Serial.println(timer);
  } else {
    switchState();
  }
}

void switchState() {
  if (state == WORK) {
    state = (timer % 8 == 0) ? LONG_BREAK : SHORT_BREAK; // Every 8th break is a long break
    timer = (state == SHORT_BREAK) ? SHORT_BREAK : LONG_BREAK;
    CircuitPlayground.playTone(500, 500); // Play tone for 500 ms at 500 Hz
  } else {
    state = WORK;
    timer = WORK_TIME;
    CircuitPlayground.playTone(1000, 500); // Higher tone for work session start
  }
  Serial.println(state == WORK ? "Work time" : (state == SHORT_BREAK ? "Short break" : "Long break"));
  isRunning = true; // Automatically start next session
}

void updateLEDs() {
  int ledCount = map(timer, 0, (state == WORK ? WORK_TIME : (state == SHORT_BREAK ? SHORT_BREAK : LONG_BREAK)), 0, 10);
  for (int i = 0; i < 10; i++) {
    if (i < ledCount) {
      CircuitPlayground.setPixelColor(i, CircuitPlayground.colorWheel(25 * i));
    } else {
      CircuitPlayground.setPixelColor(i, 0);
    }
  }
}

void resetTimer() {
  state = WORK;
  timer = WORK_TIME;
  isRunning = false;
  updateLEDs();
}

