const int pinLED = 13;
void setup() {
  Serial.begin(9600);
  pinMode (pinLED, OUTPUT);

}

void loop() {
  if (Serial.available()>0)
  {
    char option = Serial.read();
    if (option >= '1' && option <= '9')
    {
      option -= '0';
      for (int i=0;i<option; i++)
      {
        digitalWrite(pinLED, HIGH);
        delay(100);
        digitalWrite(pinLED, LOW);
        delay(200);
      }
    }
  }

}
