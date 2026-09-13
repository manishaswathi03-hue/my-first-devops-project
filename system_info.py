import datetime
import platform

print("=== System Info Checker ===")
print("Current Date & Time:", datetime.datetime.now())
print("Operating System:", platform.system())
print("OS Version:", platform.version())
print("Python Version:", platform.python_version())
print("Processor:", platform.processor())
import socket
import shutil

print("IP Address:", socket.gethostbyname(socket.gethostname()))

total, used, free = shutil.disk_usage("/")
print("Total Disk Space:", total // (2**30), "GB")
print("Used Disk Space:", used // (2**30), "GB")
print("Free Disk Space:", free // (2**30), "GB")
