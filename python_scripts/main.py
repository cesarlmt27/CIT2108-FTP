from scapy.all import *

s = socket.socket()
s.connect(("172.17.0.2",21))
ss = StreamSocket(s,Raw)

# Inicio de sesión de usuario
ss.sr(Raw("USER john_doe\r\n"))
ss.sr(Raw("PASS 123\r\n"))
ss.sr(Raw("PWD\r\n"))
ss.sr(Raw("EPSV\r\n"))

# Descarga de archivo
ss.sr(Raw("TYPE I\r\n"))
ss.sr(Raw("SIZE myfile.txt\r\n"))
ss.sr(Raw("RETR myfile.txt\r\n"))

# Cierre de sesión de usuario
ss.sr(Raw("QUIT\r\n"))

s.close()