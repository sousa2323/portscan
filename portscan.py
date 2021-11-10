import socket

domain = input(str("Enter a domain..."))

ports = [21, 23, 80, 443, 8080]

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    codigo = client.connect_ex((domain, port))
    if codigo == 0:
        print(port, "OPEN")
    else:
        print(port, "CLOSED")    