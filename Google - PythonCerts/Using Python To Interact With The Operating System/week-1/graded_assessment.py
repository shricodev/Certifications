
'''health_checks.py'''
#!/usr/bin/env python3
from network import *
import shutil
import psutil
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage <75

if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")
    
'''network.py'''
#!/usr/bin/env python3
import requests
import socket

def check_localhost():
        localhost = socket.gethostbyname('localhost')
        return localhost == "127.0.0.1"

def check_connectivity():
        request = requests.get("http://www.google.com")
        return request.status_code == int(200)
