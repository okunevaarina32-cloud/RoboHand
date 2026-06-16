#include <Servo.h>

Servo myServo;

int sensorPin = A0;
int state = 0;

void setup() {
  myServo.attach(9);
  Serial.begin(9600);
}

void loop() {

  if (Serial.available()) {
    char command = Serial.read();

    // СЖАТЬ
    if (command == 'c') {
      myServo.write(180);
      delay(1000);

      int current = analogRead(sensorPin);

      if (current > 600) {
        state = 2; // есть предмет
      } else {
        state = 1; // нет предмета
      }
    }

    // РАЗЖАТЬ
    if (command == 'o') {
      myServo.write(0);
      state = 0;
    }
  }

  Serial.println(state);
  delay(300);
}