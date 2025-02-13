
# Port Scanner

## Description
The Port Scanner is a Python-based tool that scans a range of ports on a target (IP address or domain) to identify which ports are open. It is useful for testing network security, identifying vulnerabilities, or general network diagnostics.

## Features
- Scans a range of ports on any target IP or domain.
- Identifies open ports quickly using socket connections.
- Includes error handling for hostname resolution and user interruptions.
- Displays the time taken for the scan.

## How It Works
The Port Scanner uses the Python `socket` library to attempt TCP connections to specified ports on a given target.  
- If a connection is successful, the port is marked as open.  
- The script also calculates the time taken to complete the scan.  
- Results are displayed in the terminal.

## Requirements
- Python 3.6 or above
- Libraries: No additional libraries are required (uses Python's standard library)

## Usage Instructions
1. Clone or download this project to your local machine.
2. Open a terminal in the project directory.
3. Run the script:
   bash :~ python port_scanner.py
   
4. Enter the required inputs when prompted:
   - Target: IP address or domain name (e.g., `127.0.0.1` or `example.com`)
   - Starting Port: First port number to scan (e.g., `1`)
   - Ending Port: Last port number to scan (e.g., `1024`)
5. View the results, including the open ports and the scan duration.

## File Structure
```
Port-Scanner/
│
├── port_scanner.py        # Main script for scanning ports
├── README.md              # Documentation of the project
```

## Future Improvements
- Add support for UDP port scanning.
- Integrate multithreading for faster scans.
- Implement service detection to identify services running on open ports.
- Add a graphical user interface (GUI) for easier usage.

## Credits
- Developed by [Somashekhar Hiremath]
- Inspired by network security tools and Python socket programming tutorials.
