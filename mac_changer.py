#!/usr/bin/env python3

# This is a simple script to turn off the network interface for wlan0 and eth0

# previous codes. This is not secure as it can be exploited by the user changing the input to a malicious command
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

import subprocess # importing the subprocess module to run the system commands
import optparse # importing the optparse module to parse the command line arguments

# setting up function to change the MAC address
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change is's MAC address") # adding options to the parser for interface
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address") # adding options to the parser for MAC address
    (options, arguments) = parser.parse_args() # storing value in options and arguments

    if not options.interface:
        # code to handle error
        parser.error(" [-] Please specify an interface, use --help for more information")
    elif not options.new_mac:
        # code to handle erro
        parser.error(" [-] Please specify a new MAC address, use --help for more information")    
    return options # returning the value of options to the function    

def change_mac(interface, new_mac):
    print(" [+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"]) # turns of the interface to change the mac 
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac]) # changes the MAC address to given value
    subprocess.call(["ifconfig", interface, "up"]) # turns on the interface after changing the MAC address

options = get_arguments() # getting the value of options and arguments from the function to work with change_mac function.
change_mac(options.interface, options.new_mac) # calling the function to change the MAC address

print(" [+] MAC address changed successfully to " + options.new_mac) # printing the success message after changing the MAC address