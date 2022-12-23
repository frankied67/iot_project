# iot_project
This is an Automated Plant Environment monitoring system monitoring Temperature, Humidity and Soil moisture content. This project has the ability to be expanded to include other sensors and automation including Heat lamp and led lighting.
This project uses a Raspberry pi 3, DHT11 sensor and yl moisture sensors to collect data. These sensors are attached to the Raspberry using jumper wires. 
The vcc+ jump wire from the DHT11 sensor is attached to pin 1 (3v3 power pin) on the raspberry pi. The GND- jumper wire is attached to the gound pin 9 and the remaining pin is attached to pin 11 (GPIO17) on the raspberry pi.

The moisture sensor requires a small board to convert the signal. Two jumper wires are attached to the moisture sensor and the other ends are attached to the board which has tow connectors for the jumper leads. It does not matter which cable is attached to which connector.
The other side of the board has 4 connectors for jumper wires. The ones we use on this project are the vcc, ground and DO. The remaining connector is unumportant.
The Vcc jumper cable is attache to pin 17 (3V3 power pin), the ground jumper wire to pin 20 which is a ground pin and the DO jumpoer cable is attached to pin 22 (GPIO25) on the Raspberry pi.

The python code file for this project involves:

importing the library for the blynk application
importing the Adafruit library to take readings from the sensors
importing the time library

The sensor variables are declared and initialised.

While loop runs the code infinitely to send readings to the Blynk application

