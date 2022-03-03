#import subprocess

interface = "wlan0"
new_mac = "00:11:22:33:44:66"

print('[+] Changing mac address for' + interface + " to " + new_mac)

#subprocess.call("ifconfig wlano down", shell = True)

#subprocess.call("ifconfig wlano hw ether 11:22:33:44:55:66", shell = True)

#subprocess.call("ifconfig wlano up", shell = True)
