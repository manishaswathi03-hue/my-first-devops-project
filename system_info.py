import datetime
import platform

print("=== System Info Checker ===")
print("Current Date & Time:", datetime.datetime.now())
print("Operating System:", platform.system())
print("OS Version:", platform.version())
print("Python Version:", platform.python_version())
print("Processor:", platform.processor())
