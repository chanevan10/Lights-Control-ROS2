# BlueROV2 Light Control

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
