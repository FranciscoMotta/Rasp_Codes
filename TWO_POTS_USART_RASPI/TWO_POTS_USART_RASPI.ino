void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
///////////////////////////////////////////////
  // put your main code here, to run repeatedly:
  int primerPot = analogRead(A0);
  int segundoPot = analogRead(A1);
///////////////////////////////////////////////
  String data_Send = "";
///////////////////////////////////////////////
  data_Send = data_Send + "*";
  data_Send = data_Send + "primer pot: ";
  data_Send = data_Send + primerPot;
  data_Send = data_Send + "  ";
  data_Send = data_Send + "segundo pot: ";
  data_Send = data_Send + segundoPot;
  data_Send = data_Send + "#" + "";
////////////////////////////////////////////////
  Serial.println(data_Send);
  delay(500);
}
