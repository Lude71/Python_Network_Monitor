
import csv
import subprocess
import datetime
import os

# Function 1: Validate the IPv4 address
def is_valid_ipv4(ip_address):
    ip_parts = ip_address.split(".")

    if len(ip_parts) != 4:
        return False

    for part in ip_parts:
        if not part.isdigit():
            return False

        number = int(part)

        if number < 0 or number > 255:
            return False

    return True


# Function 2: Check network connectivity
def check_connectivity(ip_address):
    try:
        result = subprocess.run(
            ["ping", "-n", "4", ip_address],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0 and "TTL=" in result.stdout:
            return "responding"
        else:
            return "no_reply"

    except subprocess.TimeoutExpired:
        return "timeout"



# Main program starts here
print("==============================")
print("   PYTHON NETWORK MONITOR")
print("==============================")


# Store multiple devices
devices = [
    {"name": "Main Router", "ip": "192.168.0.1"},
    {"name": "Local Computer", "ip": "127.0.0.1"},
    {"name": "Test Device", "ip": "192.0.2.1"}
]


# Initialize counters
online_count = 0
no_reply_count = 0
invalid_count = 0
timeout_count = 0


# Prepare the CSV report

csv_filename = "monitoring_results.csv"

write_header = (
    not os.path.exists(csv_filename)
    or os.path.getsize(csv_filename) == 0
)

with open(csv_filename, "a", newline="") as file:
    writer = csv.writer(file)

    # Write the header only for a new or empty file
    if write_header:
        writer.writerow([
            "Device Name",
            "IP Address",
            "Status",
            "Check Time"
        ])

    # Monitor each device
    for device in devices:
        device_name = device["name"]
        ip_address = device["ip"]

        print()
        print("Device Name:", device_name)
        print("IP Address:", ip_address)
        print("------------------------------")

        if is_valid_ipv4(ip_address):
            print("IPv4 format: Valid")
            print("Checking network connectivity...")

            status = check_connectivity(ip_address)

            if status == "responding":
                report_status = "Responding"
                print("Network Status:", report_status)
                online_count += 1

            elif status == "no_reply":
                report_status = "No ping reply detected"
                print("Network Status:", report_status)
                no_reply_count += 1

            elif status == "timeout":
                report_status = "Timed out"
                print("Network Status:", report_status)
                timeout_count += 1

        else:
            print("IPv4 format: Invalid")
            print("Network Status: Not checked")
            report_status = "Invalid IP address"
            invalid_count += 1

        # Record the time after checking the device
        check_time = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Append this device's result to the CSV
        writer.writerow([
            device_name,
            ip_address,
            report_status,
            check_time
        ])


# Display monitoring summary
print()
print("==============================")
print("     MONITORING SUMMARY")
print("==============================")
print("Total devices:", len(devices))
print("Responding devices:", online_count)
print("No ping reply:", no_reply_count)
print("Timed out:", timeout_count)
print("Invalid IP addresses:", invalid_count)
print("Monitoring complete.")
print("Results added to:", csv_filename)
