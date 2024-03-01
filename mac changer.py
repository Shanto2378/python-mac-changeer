#!/usr/bin/env python3

import subprocess

# This is a simple script to turn off the network interface for wlan0 and eth0
# subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
