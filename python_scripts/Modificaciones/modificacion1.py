from scapy.all import *
import random

def string():
    var = ''

    for _ in range(25):
        n = random.randint(0, 255)
        char = chr(n)
        var = var + char
    
    return var


s = socket.socket()
s.connect(("172.17.0.2",21))
ss = StreamSocket(s,Raw)

# Inicio de sesión de usuario
ss.sr1(Raw("USER john_doe\r\n"))
ss.sr1(Raw("PASS 123\r\n"))
ss.sr1(Raw("PWD\r\n"))
ss.sr1(Raw("EPSV\r\n"))

# Descarga de archivo
ss.sr1(Raw(f"TYPE {string()}\r\n"))   # Primera modificación
ss.sr1(Raw("SIZE myfile.txt\r\n"))
ss.sr1(Raw("RETR myfile.txt\r\n"))

# Cierre de sesión de usuario
ss.sr1(Raw("QUIT\r\n"))

s.close()
