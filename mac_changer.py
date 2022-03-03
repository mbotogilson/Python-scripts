import subprocess

interface = input("Interface > ")
new_mac = input("Input your new mac > ")

print('[+] Changing mac address for' + interface + " to " + new_mac)

subprocess.call("ifconfig" + interface + " down", shell = True)

subprocess.call("ifconfig" + interface + " hw ether" + new_mac, shell = True)

subprocess.call("ifconfig" + interface + " up", shell = True)
