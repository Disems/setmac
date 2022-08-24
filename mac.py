#!/usr/bin/env python

import subprocess
import optparse 

def get_argumensts():
        parser = optparse.OptionParser()
        parser.add_option("-i", "--interface", dest="interface", help="Interface to change eth0/wlan0")
        parser.add_option("-m", "--mac-adress", dest="new_mac", help="Input you new Mac Adress")
        (option, arguments) = parser.parse_args()
        if not opions.interface:
                parser.error("[-] Please specify an interface, use --help for more info.")
        elif not options.new_mac:
                parser.error("[-] Please specify a new mac, use --help for more info.") 
        return options              
 def change_mac(interface, new_mac):
        print("[+] Changing MAC adress for " + interface + " to " + new_mac)
        subprocess.call(["ifconfig", interface, "down"]) 
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])   
        subprocess.call(["ifconfig", interface, "up"])         
options = get_argumensts()
change_mac(options.interface, options.new_mac)