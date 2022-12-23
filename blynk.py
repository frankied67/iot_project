import BlynkLib             # Library for Blynk application
import RPi.GPIO as GPIO     # Library for GPIO pins
import Adafruit_DHT         # Library for the DHT11 sensor
import time                 # time library
from time import sleep

dht_sensor = Adafruit_DHT.DHT11                     # declaration of the dht11 sensor
dht_pin = 17  # 11                                  # pin for the dht11 sensor
BLYNK_AUTH = "wJZUeBg_Dq9JAH1BtX1ORcElRc2EKVaw"     # Blynk authentication code taken from setting up the application
# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# timer = BlynkTimer()

yl_channel = 25  # 22                               # declare the moisture sensor
GPIO.setmode(GPIO.BCM)                              # setup mode for the GPIO pins
GPIO.setup(yl_channel, GPIO.IN)                     # set up the moisture sensor as it does not have it's own library

while True:                                                                         # while loop
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)            # readings from the dht11 sensor
    moisture_reading = GPIO.input(yl_channel)                                       # readings from the moisture sensor
    if moisture_reading == GPIO.HIGH:                                               # if statement on what to do when the moisture is high
        blynk.virtual_write(2, 1023)                                                # virtual pin, illumination
        moisture = "Sufficient Moisture."                                           # initially printed to the terminal to test sensors were working
    else:
        blynk.virtual_write(2, 0)                                                   # else statement what to do when moisture is low
        moisture = "Low moisture, irrigation needed."
        blynk.log_event("moisture_control_")

    blynk.virtual_write(0, humidity)                                                # virtual pin for humidity
    blynk.virtual_write(1, temperature)                                             # virtual pin for temperature
    blynk.virtual_write(2, moisture)                                                #virtual pin for moisture
    print("values sent to Blynk Server!")                                           # prints to the terminal informing connection with Blynk

   # print("Moisture :", moisture)                                                    initial code printed to the console to test if sensors were working
   # print("Temperature :", temperature)                                            
   # print("Humidity :", humidity)
   # time.sleep(5)
