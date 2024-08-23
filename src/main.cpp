#include <Wire.h>

// configuring i2c buses
const PinMap PinMap_I2C_SDA[] = {
  {PB_7,  I2C1, STM_PIN_DATA(STM_MODE_AF_OD, GPIO_PULLUP, AFIO_I2C1_DISABLE)},
  {PB_9,  I2C1, STM_PIN_DATA(STM_MODE_AF_OD, GPIO_PULLUP, AFIO_I2C1_ENABLE)},
  {PB_11, I2C2, STM_PIN_DATA(STM_MODE_AF_OD, GPIO_PULLUP, AFIO_NONE)},
  {NC,    NP,   0}
};
const PinMap PinMap_I2C_SCL[] = {
  {PB_6,  I2C1, STM_PIN_DATA(STM_MODE_AF_OD, GPIO_PULLUP, AFIO_I2C1_DISABLE)},
  {PB_8,  I2C1, STM_PIN_DATA(STM_MODE_AF_OD, GPIO_PULLUP, AFIO_I2C1_ENABLE)},
  {PB_10, I2C2, STM_PIN_DATA(STM_MODE_AF_OD, GPIO_PULLUP, AFIO_NONE)},
  {NC,    NP,   0}
};

// variables
byte address = 0x30;
const int motorPin = PA1;
const int speed = 180;
const int forwardDelay = 1000;
int currentQueue = 0;

// callback for i2c
void handleReceive(int bytes) {
  String str = "";
  while (Wire.available()) {
    char c = Wire.read();
    str += String(c);
  }
  str.trim();
  Serial.println(str);
  
  switch (str[0]) {
    case 'F':
      currentQueue++;
      break;
    default:
      break;
  }
}

// drive motor
void driveMotor() {
  Serial.println("Motor on!");
  analogWrite(motorPin, speed);
  delay(forwardDelay);
  analogWrite(motorPin, 0);
  Serial.println("Motor off!");
}

// main
void setup() {

  pinMode(motorPin, OUTPUT);
  digitalWrite(motorPin, LOW);

  Serial.begin(115200);
  delay(500);

  Wire.begin(address);
  Wire.onReceive(handleReceive);
}

void loop() {
  if (currentQueue != 0) {
    driveMotor();
    currentQueue--;
  }
}