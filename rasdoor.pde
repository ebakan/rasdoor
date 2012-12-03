#include <Arduino.h>
#include <Servo.h>
Servo servo;
int pos = 0;
void setup()
{
  Serial.begin(9600);
  servo.attach(8);
}
void loop()
{
  if (Serial.available() > 0)
  {
    int val = Serial.read();
    if (val >=0 && val<=180)
    {
      pos = val;
    }
  }
  servo.write(pos);
  Serial.flush();
  delay(20);
}
