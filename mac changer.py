#!/usr/bin/env python3

# This is a simple script to turn off the network interface for wlan0 and eth0

import subprocess

interface = input("Interface > ")
new_mac = input("New MAC > ")

print(" [+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
