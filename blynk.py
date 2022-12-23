import BlynkLib
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
from time import sleep

dht_sensor = Adafruit_DHT.DHT11
dht_pin = 17  # 11
BLYNK_AUTH = "wJZUeBg_Dq9JAH1BtX1ORcElRc2EKVaw"
# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# timer = BlynkTimer()

yl_channel = 25  # 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(yl_channel, GPIO.IN)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)
    moisture_reading = GPIO.input(yl_channel)
    if moisture_reading == GPIO.HIGH:
        blynk.virtual_write(2, 1023)
        moisture = "Sufficient Moisture."
    else:
        blynk.virtual_write(2, 0)
        moisture = "Low moisture, irrigation needed."
        blynk.log_event("moisture_control_")

    blynk.virtual_write(0, humidity)
    blynk.virtual_write(1, temperature)
    blynk.virtual_write(2, moisture)
    print("values sent to Blynk Server!")

   # print("Moisture :", moisture)
   # print("Temperature :", temperature)
   # print("Humidity :", humidity)
   # time.sleep(5)
