import socket

def track_ip():
    hostname = socket.gethostname()
    ip_adress = socket.gethostbyname(hostname)
    return ip_adress
