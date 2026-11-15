import socket

host = "127.0.0.1"
ports = [22, 80, 443, 3306]

print("Checking ports on my own computer:", host)

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host, port))
    if result == 0:
        print("Port", port, "is open")
    else:
        print("Port", port, "is closed")
    s.close()
