#!/usr/bin/env python3

# This is a simple script to turn off the network interface for wlan0 and eth0

import subprocess
import optparse
import re

def user_input():
    parser = optparse.OptionParser() # create an object of OptionParser
    parser.add_option("-i", "--interface", dest = "interface", help = "Enter a valid interface by -i or --interface") # add options to the parser
    parser.add_option("-m", "--mac", dest = "new_mac", help = "Enter a valid mac_address by -m or --mac") # add options to the parser
    (options, arguments) = parser.parse_args() # parse the options and arguments
    if not options.interface: # if the user does not enter the interface
        parser.error("Enter a valid interface use --help for more info") # print the error message
    elif not options.new_mac: # if the user does not enter the mac address
        parser.error("Enter a valid mac address use --help for more info") # print the error message
    return options # return the options
    
def change_mac(interface, new_mac): # function to change the mac address
    print("[+] Changing mac for " + interface + " to " + new_mac) # print the message

    subprocess.call(["ifconfig", interface, "down"]) # turn off the interface
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac]) # change the mac address
    subprocess.call(["ifconfig", interface, "up"]) # turn on the interface

def get_current_mac(interface): # function to get the current mac address
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("UTF-8") # get the output of the ifconfig command
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result) # search for the mac address in the output

    if mac_result: # if the mac address is found
        return mac_result.group(0) # return the mac address
    else: # if the mac address is not found
        print("Could not read Mac Address") # print the message

options = user_input() # get the user input

current_mac = get_current_mac(options.interface) # get the current mac address

print("[+] Current Interface", options.interface) # print the current interface
print("[+] Current mac", current_mac) # print the current mac address

change_mac(options.interface, options.new_mac) # change the mac address

current_mac = get_current_mac(options.interface) # get the current mac address

if current_mac == options.new_mac: # if the mac address is changed
    print("[+] Mac Address is changed to ", current_mac) # print the message
else: # if the mac address is not changed
    print("Mac Adress did not get changed") # print the message