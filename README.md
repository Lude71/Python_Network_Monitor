# Python Network Monitoring Tool

## Overview

The **Python Network Monitoring Tool** is a beginner-friendly networking and Python project that checks the connectivity of specified devices using their IPv4 addresses. It records monitoring results in a CSV file and analyzes historical records to help identify devices that may require further investigation.

This project combines practical networking concepts with Python programming, file handling, error handling, and basic data analysis.

## Features

- **IPv4 validation:** Checks the format and range of IPv4 addresses.
- **Connectivity monitoring:** Uses the Windows `ping` command to test whether a device responds.
- **Multiple-device monitoring:** Checks several devices in one execution.
- **Status reporting:** Tracks responding devices, devices with no ping reply, timeouts, and invalid addresses.
- **CSV logging:** Saves device names, IP addresses, statuses, and timestamps.
- **Historical analysis:** Summarizes monitoring records and calculates response rates.
- **Error handling:** Handles timeouts and missing history files.

## Technologies Used

- Python 3
- Windows PowerShell
- CSV file handling
- Python `subprocess`, `datetime`, and `os` modules
- IPv4 addressing and ICMP ping
- Git and GitHub (for version control and project sharing)

## Project Structure

```text
Python_Network_Monitor/
├── main.py
├── history_analysis.py
├── monitoring_results.csv
├── README.md
└── practice/
    ├── ping_test.py
    ├── list_practice.py
    ├── csv_practice.py
    ├── datetime_practice.py
    └── error_practice.py
```

## Requirements

- Python 3 installed on Windows
- PowerShell or a compatible terminal
- Network access for testing reachable network devices

## How to Run

Open PowerShell and navigate to the project directory:

```powershell
cd "C:\Users\Administrator\OneDrive\Documents\PYTHON PRACTICE\Python_Network_Monitor"
```

Run the monitoring tool:

```powershell
python main.py
```

Analyze the saved monitoring history:

```powershell
python history_analysis.py
```

## Sample Results

A successful test run produced the following results:

| Device | IP Address | Result |
|---|---|---|
| Main Router | `192.168.0.1` | Responding |
| Local Computer | `127.0.0.1` | Responding |
| Test Device | `192.0.2.1` | Timed out |

The tool saves monitoring records in `monitoring_results.csv` for later analysis.

The `192.0.2.1` address belongs to a range reserved for documentation and examples. It is used here to demonstrate a timeout, not as a real production device.

## How It Works

1. The program loads a list of devices and their IP addresses.
2. Each address is checked for basic IPv4 formatting and range validity.
3. The program runs a Windows ping command to test connectivity.
4. The result and timestamp are written to the CSV report.
5. A monitoring summary displays the results.
6. The history analyzer reads previous records, groups results by device and status, and calculates response rates.

## What I Learned

Through this project, I practised:

- Python variables, data types, lists, dictionaries, loops, and functions.
- Input validation and conditional statements.
- Using `subprocess.run()` to execute operating-system commands.
- Handling timeouts and missing files.
- Writing and reading CSV files.
- Working with timestamps.
- Calculating response rates from historical records.
- Organizing a Python project into application code and practice scripts.

## Limitations

- The current tool uses Windows-specific ping arguments.
- A ping timeout does not necessarily mean a device is offline; ICMP traffic may be blocked or packets may be lost.
- The response-rate threshold is a simple project rule, not a universal networking standard.
- The tool currently runs on demand rather than monitoring continuously in the background.

## Future Improvements

- Add continuous monitoring at configurable intervals.
- Generate graphical reports of device availability.
- Add configurable device lists.
- Export summary reports.
- Introduce logging and alert notifications.
- Add automated tests and improve IP-address validation.

## Author

**Lude71**

Telecommunication and Information Engineering student developing practical skills in networking, Python programming, and network monitoring.

---

*This project is part of my hands-on learning journey toward building practical networking and IT skills.*