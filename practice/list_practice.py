# Topic : Python List

devices = ["Main Router", "Laptop", "Printer"]

print("All devices:", devices)
print("First device:", devices[0])
print("Second device:", devices[1])
print("Third device:", devices[2])

devices.append("Server")

print(devices)
print("Number of devices:", len(devices))

# Dictionaries
device = {
    "name": "Main Router",
    "ip": "192.168.0.1" 
}

print("Device name:", device["name"])
print("Device IP:", device["ip"])

devices = [
    {"name": "Main Router", "ip": "192.168.0.1"},
    {"name": "Laptop", "ip": "127.0.0.1"},
    {"name": "Test Device", "ip": "192.0.2.1"},

]

print("Device 1:", devices[0]["name"])
print("IP address:", devices[0]["ip"])

print("Device 2:", devices[1]["name"])
print("IP address:", devices[1]["ip"])

devices = [
    {"name": "Main Router", "ip": "192.168.0.1"},
    {"name": "Laptop", "ip": "127.0.0.1"},
    {"name": "Test Device", "ip": "192.0.2.1"}  
]

for device in devices:
    print("Device name:", device["name"])
    print("IP address:", device["ip"])
    print("-------------------------")
    
# Topic: Monitoring Multiple Devices (structure only)

devices = [
    {"name": "Main Router", "ip": "192.168.0.1"},
    {"name": "Laptop", "ip": "127.0.0.1"},
    {"name": "Test Device", "ip": "192.0.2.1"}
]

for device in devices:
    device_name = device["name"]
    ip_address = device["ip"]

    print("Checking:", device_name)
    print("IP address:", ip_address)
    print("--------------------")

# counter variables
online_count = 0


online_count = online_count + 1
online_count = online_count + 1

print("Responding devices:", online_count)

# writing to a text File

report = open("monitoring_report.txt", "w")

report.write("Python Network Monitoring Report\n")
report.write("Main Router: 192.168.0.1\n")
report.write("Status: Responding\n")

report.close()

print("Report saved successfully.")

with open("monitoring_report.txt", "w") as report:
          report.write("Python Network Monitoring Report\n")
          report.write("Device: Laptop\n")
          report.write("IP Address: 127.0.0.1\n")
          report.write("Status: Responding\n")

print("Report saved successfully.")
                       

