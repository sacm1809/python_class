int cont = 0;
void setup() {
  Serial.begin(9600);

}

void loop() {
  Serial.println(cont);
  cont ++; //cont=cont+1
  delay(1000);

}
