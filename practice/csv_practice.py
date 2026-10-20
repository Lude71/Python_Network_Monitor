# Writing CSC Files
import csv

with open("monitoring_results.csv", "w", newline="") as files:
    writer = csv.writer(files)

    writer.writerow(["Device Name", "IP Address", "Status"])
    writer.writerow(["Main Router", "192.168.0.1", "Responding" ])
    writer.writerow(["Local Computer", "127.0.0.1", "Responding"])
    writer.writerow(["Test Device", "192.0.2.1", "Timed out"])

print("CSV report successfully")