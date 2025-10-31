import socket

def track_ip():
    hostname = socket.gethostname()
    ip_adress = socket.gethostbyname(hostname)
    return ip_adress

def get_local_ip():
    # n'envoie rien; utilise juste la résolution de la route
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(("8.8.8.8", 80))  # adresse publique; aucun paquet n'est réellement envoyé
            ip = s.getsockname()[0]
        except OSError:
            # fallback si pas de réseau
            ip = "127.0.0.1"
    return ip

