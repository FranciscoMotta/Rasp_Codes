void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    char dato = Serial.read();
    Serial.print(dato);
    if (dato == 'a')digitalWrite(13, HIGH);
    if (dato == 'b')digitalWrite(13, LOW);
    dato = 0;
  }
}
