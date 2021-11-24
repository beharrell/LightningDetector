#include "WiFi.h"
#include "AsyncUDP.h"

const char * ssid = "<NetworkId here>";
const char * password = "<password here>";

AsyncUDP udp;
bool foundClient = false;
#define FOCUS_DO  21
#define SHUTTER_DO 19

void HandleUDPPacket(AsyncUDPPacket packet)
{
    Serial.print("UDP Packet Type: ");
    Serial.print(packet.isBroadcast()?"Broadcast":packet.isMulticast()?"Multicast":"Unicast");
    Serial.write(packet.data(), packet.length());
    Serial.println();
    if (strncmp("FOCUS",(char *)packet.data(),packet.length()) == 0)
    {
        Serial.println("Focusing");
        digitalWrite(FOCUS_DO, true);
        delay(1000);
        digitalWrite(FOCUS_DO, false);
    }
    else if  (strncmp("SHUTTER",(char *)packet.data(),packet.length()) == 0)
    {
        Serial.println("Taking photo");
        digitalWrite(SHUTTER_DO, true);
        delay(1000);
        digitalWrite(SHUTTER_DO, false);
    }

    //reply to the client
    foundClient = true;        
}



void setup()
{
    pinMode(FOCUS_DO,OUTPUT);
    pinMode(SHUTTER_DO,OUTPUT);

    Serial.begin(115200);
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    if (WiFi.waitForConnectResult() != WL_CONNECTED) {
        Serial.println("WiFi Failed");
        while(1) {
            delay(1000);
        }
    }
    if(udp.listen(1234)) {
        Serial.print("UDP Listening on IP: ");
        Serial.println(WiFi.localIP());
        udp.onPacket(HandleUDPPacket);
    }
}

void loop()
{
    delay(1000);
    //Send broadcast on port 1234
    if (foundClient == false)
    {
        udp.broadcastTo("Anyone here?", 1234);
    }
}
