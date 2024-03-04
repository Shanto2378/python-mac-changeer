    #!/usr/bin/env python3

# This is a simple script to turn off the network interface for wlan0 and eth0

import subprocess # importing the subprocess module to run the system commands
import optparse # importing the optparse module to parse the command line arguments
import re # importing the re module to use regular expressions

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

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("UTF-8") # storing the result of the ifconfig command in ifconfig_result in UTF-8 format
    # read more at: https://discuss.python.org/t/typeerror-cannot-use-a-string-pattern-on-a-bytes-like-object/30308/2
    mac_addr_src_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result) # using regular expression to search for the MAC address in the ifconfig_result

    if mac_addr_src_result:
        return mac_addr_src_result.group(0) # returning the MAC address if found to current_mac
    else:
        print(" [-] Could not read MAC address.")

options = get_arguments() # getting the value of options and arguments from the function to work with change_mac function.

current_mac = get_current_mac(options.interface) # calling the function to get the current MAC address

print(" [+] Current MAC = ", current_mac) # printing the current MAC address
change_mac(options.interface, options.new_mac) # calling the function to change the MAC address

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print(" [+] MAC address was successfully changed to ", current_mac) # printing the new MAC address
else:
    print(" [-] MAC address did not get changed.") # printing the message if the MAC address did not get changed