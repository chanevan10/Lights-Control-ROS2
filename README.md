# BlueROV2 Light Control

A ROS 2 package for controlling and managing the lighting system of the BlueROV2 underwater vehicle. This package provides various services and nodes for light control, including automatic light adjustment, fading effects, and light recommendations.

## Overview

This package provides a comprehensive solution for controlling the lighting system of the BlueROV2 underwater vehicle. It includes services for direct light control, automatic light adjustment based on environmental conditions, and advanced light recommendation systems.

## Features

- **Light Service Node**: Core service for controlling the BlueROV2 lights
- **Fade Lights**: Smooth light transitions with customizable fade effects
- **Auto Light Adjust**: Automatic light adjustment based on environmental conditions
- **Light Recommendation**: Intelligent light recommendations for optimal visibility
- **Advanced Light Recommendation**: Enhanced recommendation system with additional parameters

## Prerequisites

- ROS 2 (tested with Humble)
- Python 3.8+
- MAVROS
- pymavlink
- BlueROV2 with compatible lighting system

## Dependencies

- rclpy
- mavros_msgs
- std_srvs
- pymavlink
- builtin_interfaces

## Installation

1. Clone this repository into your ROS 2 workspace:
```bash
cd ~/ros2_ws/src
git clone <repository-url>
```

2. Build the package:
```bash
cd ~/ros2_ws
colcon build --packages-select bluerov2_control
```

3. Source your workspace:
```bash
source install/setup.bash
```

## Usage

### Light Service Node
The core service node for controlling the BlueROV2 lights:
```bash
ros2 run bluerov2_control light_service_node.py
```

### Fade Lights
For smooth light transitions:
```bash
ros2 run bluerov2_control fade_lights.py
```

### Auto Light Adjust
For automatic light adjustment:
```bash
ros2 run bluerov2_control auto_light_adjust.py
```

### Light Recommendation
For basic light recommendations:
```bash
ros2 run bluerov2_control publish_light_recommendation.py
```

### Advanced Light Recommendation
For enhanced light recommendations:
```bash
ros2 run bluerov2_control publish_advanced_light_recommendation.py
```

## Services

### SetLight Service
The package provides a custom service `SetLight.srv` for controlling the lights. The service definition includes:
- Request: Light intensity value
- Response: Success status

## Launch Files

Launch files are available in the `launch` directory for different configurations and use cases.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Maintainers

- Your Name (someone@example.com)

## Acknowledgments

- Blue Robotics for the BlueROV2 platform
- ROS 2 community for the framework
