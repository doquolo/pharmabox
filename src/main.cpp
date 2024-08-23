#include <Arduino.h>
#include <vector>
#include <Wire.h>
#include "I2CScanner.h"

// webserver
#include <WiFi.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include <ArduinoJson.h>
#include "AsyncJson.h"

// pages
#include "home.h"

const char* ssid = "PharmaBox_Test";
const char* password = "nocnocnocnoc";

// Create AsyncWebServer instance on port 80
AsyncWebServer server(80);

void setup() {

  // init serial
  Serial.begin(115200);

  // init i2c master
  Wire.begin();
  
  // begin AP
  WiFi.softAP(ssid, password);
  Serial.print("Webserver opened on: ");
  Serial.print(WiFi.localIP());
  Serial.println(":80");

  // Server paths
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
      request->send_P(200, "text/html", homePage);
  }); 
  server.on("/scan", HTTP_GET, [](AsyncWebServerRequest *request) {
    DynamicJsonDocument doc(512);
    std::vector<byte> devices;
    devices = I2CScan();
    String deviceString = "";
    for (int i = 0; i < devices.size(); i++) {
      doc.add(String(devices[i]));
      Serial.println(String(devices[i]));
    }
    String serializedJson = "";
    serializeJson(doc, serializedJson);
    request->send(200, "application/json", serializedJson.c_str());
  });
  server.on("/test", HTTP_GET, [](AsyncWebServerRequest *request) {
    if(request->hasParam("device")) {
      AsyncWebParameter* p = request->getParam("device");
      int device = p->value().toInt();
      Wire.beginTransmission(device);
      Wire.write("F\n");
      Wire.endTransmission();
    }
    request->send(200);
  });

  server.begin();
}

void loop() {
}