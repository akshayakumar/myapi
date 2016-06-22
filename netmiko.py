#!/usr/bin/env python
import os
from netmiko import ConnectHandler

example_device = {
    "device_type": "cisco_ios",
    "ip": "rilogan-sandbox-sw1",
    "username": os.environ['network_username'],
    "password": os.environ['network_password']
}

try:
    net_connect = ConnectHandler(**example_device)
    output = net_connect.send_command("show ip int brief")
    print(output)
except Exception, e:
    print(e.message)
finally:
    net_connect.disconnect()
