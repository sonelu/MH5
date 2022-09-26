# Specifications

**Rev B.1 (September 2020)**

## Dimensions

Parameter | Value | Comments
----------|-------|----------
Height                   | 48cm |
Wide                     | 51cm | with arms stretched
Depth                    | 20cm |
Weight                   | 2.15Kg | Including the batteries
Weight                   | 1.84Kg | Excluding the batteries

## Actuators

Parameter | Value | Comments
----------|-------|----------
Degrees of Freedom (DoF) | 22 |
Legs DoF (each)          | 6  | ankle pitch and roll, knee yaw and pitch, hip pitch and roll
Legs Actuators           | 6 x 2XL430 | each leg contains 3 [2XL430-W250](https://emanual.robotis.com/docs/en/dxl/x/2xl430-w250/) Dynamixel Actuators
Arms Dof (each)          | 4  | shoulder pitch and roll, elbow yaw and pitch
Arms Actuators           | 8 x XL430  | each arm contains 4 [XL430-W250](https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/) Dynamixel Actuators
Head DoF                 | 2  | pitch and yaw
Head Actuators           | 1 x 2XL430 | one [2XL430-W250](https://emanual.robotis.com/docs/en/dxl/x/2xl430-w250/) Dynamixel Actuator

## Power

Parameter | Value | Comments
----------|-------|----------
Batteries                    | 2 x 2500mAh 3S LiPo batteries | Batteries are located in the feet and are hot-swap; there is no need to turn off the main controller to change the batteries
External power           | 2.5mm power jack 12V       | Optionally the robot can be powered with a 12V power adapter using a standard 2.5mm barrel jack
Autonomy                 | 3 hours | (preliminary estimates)
Monitoring               | voltage | ADC used to provide reading for Dynamixel bus voltage, 5V railing and 3.3V railing.

## Electronics

Parameter | Value | Comments
----------|-------|----------
Main controller          | Raspberry Pi CM4 8GB RAM | We use the [Waveshare CM4 IO Board A](https://www.waveshare.com/cm4-io-base-a.htm) to expand the peripherals. 
Add on board             | [Robotics HAT for Raspberry Pi](https://github.com/sonelu/SPR2005) | The board includes:<br>1. high speed dual Dynamixel bus<br>2. IMU (Gyroscope and Accelerometer)<br>3. 5V 3A power switch for RPi<br>4. ADC for monitoring power<br>5. WM8960 codec with stereo mics and speakers 2 x 1W output<br>6. PWM fan control<br>7. USB to UART converter for direct USB console access for RPi
Foot sensors             | [SPR2010](https://github.com/sonelu/SPR2010) | Each foot includes a circuit that:<br>1. ideal diode allowing LiPo batteries hot-swap<br>2. battery voltage and current monitoring with 4 LED level indicator, low voltage buzzer and very low voltage cut-off<br>3. four force sensing resistors (FSR) for accurate positioning of the CoM<br>4. Dynamixel bus communication interface up to 2Mbs
Display                  | [Waveshare 2.4" TFT display](https://www.waveshare.com/product/displays/lcd-oled/lcd-oled-3/2.4inch-lcd-module.htm) | A 2.4'' 320x 240 TFT display connected on SPI with console support
Camera                   | Two [RPi FPC Cameras MIni Size](https://www.waveshare.com/product/raspberry-pi/cameras/rpi-fpc-camera.htm) | Connected on the two CSI camera connectors on the IO Board, 69.8 degree FoV, max 1080p30
WiFi                     | Built-in 5Ghz frequency -WiFi and second dongle | The built in configures a low-latency (5GHz band) Access Point (AP) and the second Wi-Fi can connect to an exiting infrastructure. It is especially efficient for running distributed ROS nodes
Bluetooth                | Builtin Bluetooth 5.0 BLE | [Bluetooth keyboard](https://www.amazon.co.uk/Rii-Mini-Bluetooth-Wireless-Keyboard-Black/dp/B010WMB6DK/) for remote control and interface navigation.

## Software

Parameter | Value | Comments
----------|-------|----------
OS        | Raspbian (Debian Buster) | Kernel drivers added for:<br>- SC16IS762 (SPI to UART dual bus used for Dynamixel actuators)<br>- ST7789V (TFT display)<br>- WM8960 (sound)<br>- ADS1015 (for voltage monitoring ADC)<br>- fan_control
Software                 | ROS Noetic | ROS Noetic is installed using [RoboStack](https://github.com/RoboStack/ros-noetic)
Custom ROS packages      |[here](https://github.com/sonelu/mh5_robot) | - Dynamixel controller<br>- UI for robot TFT<br>- URDF with support for RViz and Gazebo<br>- "director" package that that process scripted moves<br>- vision (in progress)

## Future plans

There are a number of exciting upgrades to the platform that we expect to deliver soon:

Area   | Improvement
-------|-------------|
2nd Controller | Add a second controller Raspberry Pi CM4 in the head for vision processing with dedicated add-on board for cameras, power, fan and console access.
Coral support  | Integrate a Coral Board M.2 ([B+M version](https://coral.ai/products/m2-accelerator-bm)) using the M-key connector on the Waveshare IO Board
