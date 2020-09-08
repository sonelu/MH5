# MH5

Humanoid Robot MH5

MH5 is an affordable 22 DOF humanoid robot intended for research and academic study.

<img src="./img/IMG_3766_small.jpg?raw=true" width="500px">

## Specifications

Parameter | Value | Comments
----------|-------|----------
Height                   | 48cm |
Weight                   | 2.15Kg | Including the batteries
Weight                   | 1.84Kg | Excluding the batteries 
Degrees of Freedom (DoF) | 22 | 6 DoF for each leg, 4 DoF for each arm, 2 DoF for head
Actuators                | 6 x XL430, 7 x  2XL430 | Legs and head use Dynamixel 2XL430 actuators, arms use XL430
Power                    | 2 x 2500mAh LiPo batteries | Batteries are located in the feet and are hot-swap; there is no need to turn off the main controller to change the batteries
External power           | 2.5mm power jack 12V       | Optionally the robot can be powered with a 12V power adapter using a standard 2.5mm barrel jack
Autonomy                 | 3 hours | (preliminary estimates)
Main controller          | Raspberry Pi 4 4GB RAM
Add on board             | [Robotics HAT for Raspberry Pi](https://github.com/sonelu/SPR2005) | The board includes: high speed dual Dynamixel bus, IMU, 5V 3A power switch for RPi, ADC for monitoring power, WM8960 codec with stereo mics and speakers, PWM fan control.
Hot-swap circuits        | one in each foot | Each foot includes a circuit that implements an ideal diode and allows the LiPo batteries to be hot-swapped without damage to the cables or the main controller
Display                  | [Adafruit 2.0" IPS display](https://www.adafruit.com/product/4311) | A 320x 240 IPS TFT display connected on SPI with console support
Camera                   | Two [HBV-1517](https://www.amazon.co.uk/Camera-Module-HBV-1517-Wide-Angle-Install/dp/B07V9H7Z49) | Max resolution 1280 x 1024, USB connected directly to Raspberry Pi
WiFi                     | Built-in 5Ghz frequency -WiFi and second dongle | The built in configures a low-latency (5GHz band) Access Point (AP) and the second Wi-Fi can connect to an exiting infrastructure. It is especially efficient for running distributed ROS nodes.
Software                 | ROS Neotic | robot packages available [here](https://github.com/sonelu/mh5_robot)
