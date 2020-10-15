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
Batteries                    | 2 x 2500mAh LiPo batteries | Batteries are located in the feet and are hot-swap; there is no need to turn off the main controller to change the batteries
External power           | 2.5mm power jack 12V       | Optionally the robot can be powered with a 12V power adapter using a standard 2.5mm barrel jack
Autonomy                 | 3 hours | (preliminary estimates)
Monitoring               | voltage | ADC used to provide reading for Dynamixel bus voltage, 5V railing and 3.3V railing.

## Electronics

Parameter | Value | Comments
----------|-------|----------
Main controller          | Raspberry Pi 4 4GB RAM
Add on board             | [Robotics HAT for Raspberry Pi](https://github.com/sonelu/SPR2005) | The board includes:<br>1. high speed dual Dynamixel bus<br>2. IMU (Gyroscope and Accelerometer)<br>3. 5V 3A power switch for RPi<br>4. ADC for monitoring power<br>5. WM8960 codec with stereo mics and speakers 2 x 1W output<br>6. PWM fan control<br>7. USB to UART converter for direct USB console access for RPi
Hot-swap circuits        | one in each foot | Each foot includes a circuit that implements an ideal diode and allows the LiPo batteries to be hot-swapped without damage to the cables or the main controller
Display                  | [Adafruit 2.0" IPS display](https://www.adafruit.com/product/4311) | A 2.0'' 320x 240 IPS TFT display connected on SPI with console support
Camera                   | Two [HBV-1716HD](https://www.banggood.com/HBV-1716HD-2MP-OV2710-HD-1080P-CMOS-Camera-Module-with-USB-Interface-Free-Driver-Fixed-Focus-100-Degree-p-1709172.html?cur_warehouse=CN) | Max resolution 1920 x 1080, USB connected directly to Raspberry Pi, field of view 60 degrees
WiFi                     | Built-in 5Ghz frequency -WiFi and second dongle | The built in configures a low-latency (5GHz band) Access Point (AP) and the second Wi-Fi can connect to an exiting infrastructure. It is especially efficient for running distributed ROS nodes
Bluetooth                | Builtin Bluetooth 5.0 BLE | [Bluetooth keyboard](https://www.amazon.co.uk/Rii-Mini-Bluetooth-Wireless-Keyboard-Black/dp/B010WMB6DK/) for remote control and interface navigation.

## Software

Parameter | Value | Comments
----------|-------|----------
OS        | Raspbian (Debian Buster) | Kernel drivers added for:<br>- SC16IS762 (SPI to UART dual bus used for Dynamixel actuators)<br>- ST7789V (TFT display)<br>- WM8960 (sound)<br>- ADS1015 (for voltage monitoring ADC)<br>- fan_control
Software                 | ROS Neotic | ROS Neotic is installed from source using the "robot" distro
Custom ROS packages      |[here](https://github.com/sonelu/mh5_robot) | - Dynamixel controller<br>- UI for robot TFT<br>- URDF with support for RViz and Gazebo<br>- "director" package that that process scripted moves<br>- vision (in progress)

## Future plans

There are a number of exciting upgrades to the platform that we expect to deliver soon:

Area   | Improvement
-------|-------------|
~~Vision~~ | ~~Updated cameras with 100 degrees FoV and more fps options~~
Foot Sensors | Soles with 4 force sensing resistors (FSR) for accurate positioning of the CoM. Information is exchanged over the Dynamixel bus.
Battery Management | There is currently in development an improved version of the hot-swap electronics that will include low-battery buzzer and cutoff for battery protection.
Display    | Increase size of display to 2.8 inch to improve readability
