import socket
from datetime import datetime

target = input("Enter the target IP address: ")

def port_scanner(target):
    try:
        ip = socket.gethostbyname(target)

        print(f"Scanning the target {ip}")
        print(f"Time started: {datetime.now()}")

        for port in range(20, 90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} : open")
            sock.close()
    except socket.gaierror:
        print("Host cannot be resolved")
    except socket.error:
        print("Could not connect to the server")

port_scanner(target)
