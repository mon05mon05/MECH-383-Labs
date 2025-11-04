/*
Notes : 
  - "motor_control.ino" must be in a folder named "motor_control"
*/



#include <Arduino.h>

// Pin definition
int SENSOR_PIN = 0;  // center pin of the potentiometer
int RPWM_Output = 5; // Arduino PWM output pin 5; connect to IBT-2 pin 1 (RPWM)
int LPWM_Output = 6; // Arduino PWM output pin 6; connect to IBT-2 pin 2 (LPWM)
int ENCODER_A = 2;                        // Encoder channel A (interrupt pin)
int ENCODER_B = 3;                        // Encoder channel B (interrupt pin not necessary)

// Counters
volatile long pos = 0;                    // Encoder position; signed long (32-bit)
volatile long max_pos = 2147483647;       // Maximum value of signed long; used to prevent overflow

void setup()
{
  Serial.begin(9600); // serial communication with the computer

  // Setup motor control pins
  pinMode(RPWM_Output, OUTPUT);
  pinMode(LPWM_Output, OUTPUT);

  // Setup encoder
  pinMode(ENCODER_A, INPUT_PULLUP);                                      // WARNING: CH-A signal nominally high
  pinMode(ENCODER_B, INPUT_PULLUP);                                      // WARNING: CH-B signal nominally high
  attachInterrupt(digitalPinToInterrupt(ENCODER_A), encoderISRA, CHANGE); // interrupt on CH-A only
  attachInterrupt(digitalPinToInterrupt(ENCODER_B), encoderISRA, CHANGE);
  
  delay(100); // Why?
}

void loop() {
  int sensorValue = analogRead(SENSOR_PIN);
  // Sensor value is in the range 0-1023 (10-bit ADC)
  // 0-511 for reverse rotation; 512-1023 for forward rotation
  if (sensorValue < 512) {
    // Reverse rotation
    int reversePWM = (511 - sensorValue) / 2;
    analogWrite(LPWM_Output, 0);
    analogWrite(RPWM_Output, reversePWM);
  }
  else {
    // Forward rotation
    int forwardPWM = (sensorValue - 512) / 2;
    analogWrite(LPWM_Output, forwardPWM);
    analogWrite(RPWM_Output, 0);
  }

  // Send count via serial; use "println" to send a string; use "write" for improved performance
  Serial.println(String(sensorValue) + ", " + String(pos) + ", " + String(digitalRead(ENCODER_A)) + ", " + String(digitalRead(ENCODER_B))); // pos updated in the ISR

  delay(100/1024);
}

void encoderISRA() {
  // Encoder interrupt service routine; detect CH-A state transition, then check state of CH-B (HIGH/LOW)
  // CASE 1: LOW-HIGH transition on CH-A
  if (digitalRead(ENCODER_A)){
    if (digitalRead(ENCODER_B)){ //CH-B is HIGH -> Negative increment
      if (pos == -max_pos){ //RESET
        pos = 0;
      }
      else{
        pos--;
      }
    }
    else{ //CH-B is LOW -> Positive increment
      if (pos == max_pos){ //RESET
        pos = 0;
      }
      else{
        pos++;
      }
    }
  }
  else{ //CH-A is LOW
    if (digitalRead(ENCODER_B)){ //CH-B is HIGH -> Positive increment
      if (pos == max_pos){ //RESET
        pos = 0;
      }
      else{
        pos++;
      }
    }
    else{ //CH-B is LOW -> Lower increment
      if (pos == -max_pos){ //RESET
        pos = 0;
      }
      else{
        pos--;
      }
    }
  }
}