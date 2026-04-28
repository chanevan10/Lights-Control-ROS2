import rclpy
import csv
from scipy import stats
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor
import matplotlib.pyplot as plt
import subprocess
import math
import time
import threading
from bluerov2_control.srv import SetLight

from sensor_msgs.msg import BatteryState
from std_msgs.msg import Bool, Float32


class BatteryNotifierNode(Node):
    def __init__(self):
        super().__init__('battery_notifier_node')

        SENSOR_QOS = rclpy.qos.qos_profile_sensor_data

        # subscribe to battery warning topic
        self.warning_subscriber = self.create_subscription(Bool, '/battery_warning', self.warning_callback, SENSOR_QOS)

        # publish light levels to the headlights
        self.client = self.create_client(SetLight, 'light_control')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /light_control service...')

        # flashing state thread management
        self._flashing = False
        self._flash_lock = threading.Lock()

    def send_light_command(self, brightness_value: float):
        request = SetLight.Request()
        request.data = brightness_value

        future = self.client.call_async(request)
        future.add_done_callback(self.light_service_response)

    def _flash_once(self, on_dur: float, off_dur: float):
        self.send_light_command(1.0)
        time.sleep(on_dur)
        self.send_light_command(0.0)
        time.sleep(off_dur)

    def warning_callback(self, msg: Bool):
        # flashes headlights and other visual indicators to alert the user of low battery
        if msg.data:
            # Example pattern: 3x0.1s, then 3x0.2s, then 3x0.1s
            sequence = [(3, 0.1, 0.1), (3, 0.2, 0.2), (3, 0.1, 0.1)]
            with self._flash_lock:
                if self._flashing:
                    return
                self._flashing = True

            def worker():
                for _ in range(3):
                    self._flash_once(0.1, 0.1)
                for _ in range(3):
                    self._flash_once(0.2, 0.2)
                for _ in range(3):
                    self._flash_once(0.1, 0.1)
                self._flashing = False

            thr = threading.Thread(target=worker, daemon=True)
            thr.start()
            
    
def main(args=None):
    rclpy.init(args=args)
    node = BatteryNotifierNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()