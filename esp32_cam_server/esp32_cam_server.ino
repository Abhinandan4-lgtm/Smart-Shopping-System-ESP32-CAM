#include <WiFi.h>
#include <WebServer.h>
#include <esp32cam.h>

const char* WIFI_SSID = "YOUR_WIFI_NAME";
const char* WIFI_PASS = "YOUR_WIFI_PASSWORD";

WebServer server(80);

static auto hiRes = esp32cam::Resolution::find(800, 600);

void serveJpg() {
  auto frame = esp32cam::capture();
  if (!frame) {
    server.send(503, "", "");
    return;
  }

  server.setContentLength(frame->size());
  server.send(200, "image/jpeg");
  frame->writeTo(server.client());
}

void handleCam() {
  esp32cam::Camera.changeResolution(hiRes);
  serveJpg();
}

void setup() {
  Serial.begin(115200);

  using namespace esp32cam;
  Config cfg;
  cfg.setPins(pins::AiThinker);
  cfg.setResolution(hiRes);
  cfg.setJpeg(80);
  cfg.setBufferCount(2);

  Camera.begin(cfg);

  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) delay(500);

  Serial.println(WiFi.localIP());

  server.on("/cam-hi.jpg", handleCam);
  server.begin();
}

void loop() {
  server.handleClient();
}
