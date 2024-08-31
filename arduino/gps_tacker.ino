#include <TinyGPSPlus.h>
#include <HardwareSerial.h>

static const int RXPin = 4, TXPin = 3;
static const uint32_t GPSBaud = 4800;

TinyGPSPlus gps;
HardwareSerial ss(1);

void setup() {
  Serial.begin(115200);
  ss.begin(9600, SERIAL_8N1, 16, 17);
}

void loop() {
  while (ss.available() > 0) {
    if (gps.encode(ss.read())) {
      displayInfo();
    }
  }

  if (millis() > 5000 && gps.charsProcessed() < 10) {
    Serial.println("No GPS detected: check wiring.");
    while (true);
  }
}

void displayInfo() {
  if (gps.location.isValid()) {
    Serial.print(gps.location.lat(), 6);
    Serial.print(",");
    Serial.print(gps.location.lng(), 6);
    Serial.println();
  }
}







