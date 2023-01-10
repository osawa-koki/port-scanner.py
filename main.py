import socket

host = "example.com"
start_port = 50
end_port = 100

for port in range(start_port, end_port+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    sock.close()
