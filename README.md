# CHOMPEE
Pasteable sensor patches for detecting chewing using MQTT, Paho, Nano 33 IoT, and the following sensors:

**Vibration sensor** below the ear to detect vibrations.  The following link will take you through the connections for this sensor/microcontroller combination: https://learn.sparkfun.com/tutorials/piezo-vibration-sensor-hookup-guide

**Flex sensor** in inner arm of glasses to measure contractions in temporalis muscle. The following link will take you through the connections for this sensor/microcontroller combination: https://learn.sparkfun.com/tutorials/flex-sensor-hookup-guide/all

**IR distance sensor** using MAX30105 breakout worn on chin to detect chewing motions.  The arduino code explains the hookups between the 33 IoT and MAX30105

**The Python script** runs on the terminal and subscribes to the MQTT broker for published sensor data from the various patches and saves the data to a CSV file in the same folder.

