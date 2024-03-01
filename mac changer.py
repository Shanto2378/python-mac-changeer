#!/usr/bin/env python3

# This is a simple script to turn off the network interface for wlan0 and eth0

import subprocess

interface = "wlan0"
new_mac = "00:11:22:33:44:55"

print(" [+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

print("vs linux test")