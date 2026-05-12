# MAVROS Battery Monitor and Notifier Nodes
This directory contains the nodes that calculate 0 current draw voltage, used to determine battery % and use the robot's lights to notify the users when it is low battery

## Battery Monitor:
* This node currently works, subscribing to the /mavros/battery topic to get voltage and current readings over 30s.
* Then it plots voltage vs current, resulting in a linear relation between the two most of the time.
* Finding the y-intercept of this plot gives the voltage at 0 current draw, and if that number is under the nominal battery voltage, it sends a warning to the base station, and publishes to a topic for the battery notifier to use

## Battery notifier: 
* This node has yet to be tested
* It subscribes to the notifier topic to know when the battery % is low
* It should use bluerov2_control's light service to control the lights to warn the user when the topic publishes TRUE

### TODOs
* need to test the notifier
* figure out which node lives where
