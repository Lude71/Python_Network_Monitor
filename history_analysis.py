
# Topic: Reading and Analyzing CSV History

import csv

# CSV file containing monitoring history
csv_filename = "monitoring_results.csv"

# Initialize counters and dictionaries
total_records = 0
status_counts = {}
device_counts = {}

devices_to_investigate = 0
devices_acceptable = 0


# Read and analyze the CSV history
try:
    with open(csv_filename, "r", newline="") as file:
        reader = csv.reader(file)

        # Skip the column headings
        next(reader, None)

        # Read each monitoring record
        for row in reader:
            # Skip incomplete records
            if len(row) < 4:
                continue

            device_name = row[0]
            ip_address = row[1]
            status = row[2]
            check_time = row[3]

            # Count total records
            total_records += 1

            # Count each status across all devices
            if status in status_counts:
                status_counts[status] += 1
            else:
                status_counts[status] = 1

            # Create an entry for a new device
            if device_name not in device_counts:
                device_counts[device_name] = {}

            # Initialize a new status for this device
            if status not in device_counts[device_name]:
                device_counts[device_name][status] = 0

            # Increment this device's status count
            device_counts[device_name][status] += 1

except FileNotFoundError:
    print("Error: Monitoring history file was not found.")
    print("Run main.py first to generate monitoring results.")
    raise SystemExit(1)


# Display the monitoring history report
print("==============================")
print("   MONITORING HISTORY REPORT")
print("==============================")

print("Total monitoring records:", total_records)


# Display the overall status breakdown
print()
print("Status Breakdown:")

for status, count in status_counts.items():
    print(status + ":", count)


# Display the status breakdown for each device
print()
print("Device Breakdown:")

for device_name, counts in device_counts.items():
    print(device_name + ":")

    for status, count in counts.items():
        print("  " + status + ": " + str(count))


# Calculate and display device response rates
print()
print("Device Response Rates:")

for device_name, counts in device_counts.items():
    total_checks = sum(counts.values())
    successful_checks = counts.get("Responding", 0)

    # Calculate the response rate safely
    if total_checks > 0:
        response_rate = (
            successful_checks / total_checks
        ) * 100
    else:
        response_rate = 0

    # Classify the device based on the 80% threshold
    if response_rate < 80:
        result = "Needs investigation"
        devices_to_investigate += 1
    else:
        result = "Response rate acceptable"
        devices_acceptable += 1

    print(
        device_name + ": "
        + str(round(response_rate, 2)) + "% - "
        + result
    )


# Display the monitoring summary
print()
print("MONITORING SUMMARY")
print("------------------")
print("Devices analyzed:", len(device_counts))
print("Needs investigation:", devices_to_investigate)
print("Response rate acceptable:", devices_acceptable)

print()
print("History analysis complete.")
