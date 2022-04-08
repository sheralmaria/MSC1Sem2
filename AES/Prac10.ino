#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266_SSL.h>
//You should get Auth Token in the Blynk App.
//Go to the Project Settings(nut icon)-> Auth Tokens -> Copy All
char auth[]="YourAuthToken";
char said[]="YourNetworkName"; //WiFi Name
char pass[]="YourPassword"; //Wifi Password
void setup() {
  // put your setup code here, to run once:
  //Debug Console
  Serial.begin(9600);
  Blynk.begin(auth,said,pass);
}

void loop() {
  // put your main code here, to run repeatedly:
 Blynk.run();
}
