import socket

def get_local_ip():
    # Get the local IP address of the machine
    try:
        host_name = socket.gethostname()
        local_ip = socket.gethostbyname(host_name)
        return local_ip
    except socket.gaierror:
        return None

def scan_network(ip_prefix, ports):
    devices = {}
    local_ip = get_local_ip()

    for i in range(1, 256):  # Assuming a typical IPv4 network with a /24 subnet (256 addresses)
        ip = f"{ip_prefix}.{i}"
        open_ports = []
        for port in ports:
            try:
                # Attempt to create a socket connection to the current port
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1)  # Adjust the timeout as needed
                    s.connect((ip, port))
                    open_ports.append(port)
            except (socket.timeout, ConnectionRefusedError):
                pass  # Port not open
        if open_ports:
            devices[ip] = open_ports

    if local_ip and local_ip.startswith(ip_prefix):
        local_ports = []
        for port in ports:
            try:
                # Attempt to create a socket connection to the current port on the local machine
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1)  # Adjust the timeout as needed
                    s.connect((local_ip, port))
                    local_ports.append(port)
            except (socket.timeout, ConnectionRefusedError):
                pass  # Port not open
        if local_ports:
            devices[local_ip] = local_ports

    return devices

if __name__ == "__main__":
    network_prefix = "192.168.1"  # Change this to your network's IP prefix
    target_ports = [80, 443, 22]  # Change this to the ports you want to check
    
    devices_found = scan_network(network_prefix, target_ports)
    
    if devices_found:
        print("Devices in the network with open ports:")
        for device, open_ports in devices_found.items():
            print(f"Device: {device}, Open Ports: {', '.join(map(str, open_ports))}")
    else:
        print("No devices found in the network.")
