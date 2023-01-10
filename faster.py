import concurrent.futures
import socket

host = "example.com"
start_port = 50
end_port = 100

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((host, port))
    if result == 0:
        return f"🪟 Port {port} is open."
    else:
        return f"🚪 Port {port} is closed."

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(check_port, host, port) for port in range(start_port, end_port+1)]

for result in concurrent.futures.as_completed(results):
    print(result.result())
