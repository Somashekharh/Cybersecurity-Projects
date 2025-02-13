import socket
from datetime import datetime

# Banner
print("-" * 50)
print("Welcome to the Port Scanner")
print("-" * 50)

# Input: Target and Port Range
target = input("Enter the target (IP or domain): ")
start_port = int(input("Enter the starting port (e.g., 1): "))
end_port = int(input("Enter the ending port (e.g., 1024): "))

print(f"\nScanning target: {target}")
print(f"Scanning ports from {start_port} to {end_port}...\n")
print("-" * 50)

# Record the start time
start_time = datetime.now()

# Port Scanning Logic
try:
    for port in range(start_port, end_port + 1):
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set timeout for faster scanning
            s.settimeout(0.5)
            # Try to connect to the target on the specified port
            result = s.connect_ex((target, port))
            if result == 0:  # Port is open
                print(f"Port {port}: Open")
            
except KeyboardInterrupt:
    print("\nScan interrupted by user.")
except socket.gaierror:
    print("\nHostname could not be resolved.")
except socket.error:
    print("\nServer not responding.")

# Record the end time
end_time = datetime.now()

# Duration of the scan
print("-" * 50)
print(f"Scan completed in: {end_time - start_time}")
print("-" * 50)
