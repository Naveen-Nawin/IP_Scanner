import platform
import subprocess
import ipaddress

def ping_ip(ip):
    # Ping the IP and return True if it's reachable
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", str(ip)]
    try:
        output = subprocess.check_output(command)
        return True
    except subprocess.CalledProcessError:
        return False

def scan_ip_range(start_ip, end_ip):
    # Convert start and end IPs to their integer equivalents
    start_ip = ipaddress.IPv4Address(start_ip)
    end_ip = ipaddress.IPv4Address(end_ip)

    # Iterate through the IP range
    for ip_int in range(int(start_ip), int(end_ip) + 1):
        ip = ipaddress.IPv4Address(ip_int)
        if ping_ip(ip):
            print(f"{ip} is active")
        else:
            print(f"{ip} is not active")

if __name__ == "__main__":
    start_ip = input("Enter the start IP (e.g., 192.168.0.100): ")
    end_ip = input("Enter the end IP (e.g., 192.168.0.108): ")
    
    print(f"Scanning IP range {start_ip} to {end_ip}")
    scan_ip_range(start_ip, end_ip)
