
# import subprocess
# output = []
# output = subprocess.check_output('sudo nmap -sP -n 192.168.255.0/24', shell=True).decode()

# print(output)
from yeelight import discover_bulbs

bulbs = discover_bulbs();

ipBulb = bulbs[0]['ip'];

import getmac
ip_mac = getmac.get_mac_address(ip=ipBulb)

print(ip_mac)

