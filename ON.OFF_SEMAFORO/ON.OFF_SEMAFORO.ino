//edison miramag
//sofia chamorro
//felipe diaz 
int a=0;
int estado=0;
int b=0;
void setup() {
  // put your setup code here, to run once:
  pinMode(2,OUTPUT);
  pinMode(2,INPUT);
  pinMode(4,OUTPUT);
  pinMode(4,INPUT);
  pinMode(7,OUTPUT);
  pinMode(7,INPUT);
  pinMode(8,OUTPUT);
  pinMode(8,INPUT);

}
void loop() {
  // put your main code here, to run repeatedly:
  a=digitalRead(2);
  if((a==HIGH)&&(b==LOW)){
    estado=1-estado;
    delay(40)   
} 
  a=b;
  if(estado==1){
     digitalWrite(2,HIGH);
  }else{
    digitalWrite(2,LOW);
  }

   a=digitalRead(4);
  if((a==HIGH)&&(b==LOW)){
    estado=1-estado;
    delay(40)   
  } 
  a=b;
  if(estado==1){
     digitalWrite(4,HIGH);
  }else{
    digitalWrite(4,LOW);
  }
   a=digitalRead(7);
  if((a==HIGH)&&(b==LOW)){
    estado=1-estado;
    delay(40)   
  } 
  a=b;
  if(estado==1){
     digitalWrite(7,HIGH);
  }else{
    digitalWrite(7,LOW);
  }

  a=digitalRead(8);
  if((a==HIGH)&&(b==LOW)){
    estado=1-estado;
    delay(40)   
  } 
  a=b;
  if(estado==1){
     digitalWrite(8,HIGH);
  }else{
    digitalWrite(8,LOW);
  }
}
   
