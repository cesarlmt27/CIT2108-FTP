from scapy.all import *

s = socket.socket()
s.connect(("172.17.0.2",21))
ss = StreamSocket(s,Raw)

# Inicio de sesión de usuario
ss.sr1(Raw("USER john_doe\r\n"))
ss.sr1(Raw("PASS 123\r\n"))
ss.sr1(Raw("PWD\r\n"))    
ss.sr1(Raw(" "))    # Tercera modificación

# Descarga de archivo
ss.sr1(Raw("TYPE I\r\n"))
ss.sr1(Raw("SIZE myfile.txt\r\n"))
ss.sr1(Raw("RETR myfile.txt\r\n"))

# Cierre de sesión de usuario
ss.sr1(Raw("QUIT\r\n"))

s.close()
