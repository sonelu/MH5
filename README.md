# Humanoid Robot MH5

MH5 is an affordable 22 DOF humanoid robot intended for research and academic study.

<img src="./img/IMG_3766_small.jpg?raw=true" width="250px">  <img src="./img/IMG_3767_small.jpg?raw=true" width="250px"> 

## Name

The name MH5 derives from being the 5th model in the "Mini Humanoid" series. That being
said, in the most pure Asimovian fashion, robots have "humanized" names, in this case they
go by the name **"Miha"**. Incidentally "miha" is short for "my daughter" in Spanish, so please
refer to the robot as a she (most certainly not as "it")!

## Design Principles

When designing Miha we have considered the following principles:

1. **Affordable**: Traditionally, complex humanoid robots are expensive and difficult to afford. Costs tend to grow exponentially with the size of the robot and, while the costs of electronics follows the same downward trajectory that applies to other consumer electronic products, the mechanical parts do not see such a trend. We therefore have considered a design that offers enough volume to permit high performance computing at edge while still minimizing the requirements for the actuators.

2. **Complex but not complicated**: Toy robots are fun but useless when designing complex ML models or robotics frameworks. To provide utility, the robots need to have a degree of complexity that will warrant innovative ML models and robotics frameworks. We believe 22 DoF is a minimum that reflects the need for studying bipedal locomotion and interaction. A good array of sensors (position, effort, vision, sound, foot pressure, etc.) and processing abilities needs to complement this array of performing actuators.

3. **Easily serviceable and expandable**: Humanoid robots have a very tough life: because a lot of the research is still in infancy accidents happen and robots break quite often. Many of the platforms available on the market are not user serviceable which means significant downtime in research until the robots are returned from service. Miha is designed to be be easily serviced by any user with some minimum technical skills: parts are easily available and standard (Raspberry Pi, Dynamixel Servos) and frames are 3D printable or will be available as spares. Due to the modular nature of the frames, there is also very easy for users to design and 3D print custom frames that would provide the required functionally for a project at hand.

4. **Open and based on standardized framework**: We aim to release as much as possible from the design of the robot as opensource (hardware and software) and we will encourage the community to contribute and expand this base. We are integrating standard frameworks (ROS, TFLite, etc.) with the robot.

## Specifications

A list of complete specifications is provided [here](specifications.md).
