void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int a = analogRead(A0);
  /*CONCATENACION DE CARACTERES DE UNA CADENA DE DATOS*/
  String payload = "";
          payload = payload + "*";
          payload = payload + a;
          payload = payload + "#" + "";
  Serial.println(payload);
  delay(1000);
}
