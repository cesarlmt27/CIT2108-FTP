# Protocolo FTP
> Con el objetivo de entender y analizar el tráfico asociado al protocolo FTP, se configura un servidor FTP (Pure-FTPd) y un cliente FTP (Curl) haciendo uso de Docker, para establecer una comunicación entre ambos; y haciendo uso de Wireshark capturar el tráfico generado.


## Tabla de contenidos
* [Docker (Servidor FTP)](#docker-servidor-ftp)
* [Configuración del Servidor FTP (Pure-FTPd)](#configuración-del-servidor-ftp-pure-ftpd)
* [Docker (Cliente FTP)](#docker-cliente-ftp)
* [Comandos usados en el cliente FTP (Curl)](#comandos-usados-en-el-cliente-ftp-curl)


## Docker (Servidor FTP)

### Crear imagen de Docker del servidor FTP:
```
docker build -t pure-ftpd -f ~/Documents/server.Dockerfile .
```

### Ejecutar el contenedor en modo interactivo:
```
docker run -it --privileged --name ftp_server pure-ftpd
```

## Configuración del Servidor FTP (Pure-FTPd)

### Crear un usario FTP:
```
pure-pw useradd john_doe -u ftpuser -g ftpgroup -d /root/ftphome/john_doe/
```
Luego de ejecutar el comando se solicitará ingresar una contraseña para el usuario.
Es importante crear la carpeta del usuario nuevo. Ej: `mkdir /root/ftphome/john_doe`
También dar permisos para leer, escribir y ejecutar en la carpeta. Ej: `chmod 777 /root/ftphome/john_doe`

### Actualizar la base de datos FTP después de agregar a un nuevo usuario:
```
pure-pw mkdb
```

### Establecer enlaces simbólicos para algunos archivos:
```
ln -s /etc/pure-ftpd/pureftpd.passwd /etc/pureftpd.passwd && \
ln -s /etc/pure-ftpd/pureftpd.pdb /etc/pureftpd.pdb && \
ln -s /etc/pure-ftpd/conf/PureDB /etc/pure-ftpd/auth/PureDB
```

### Dar propiedad del directorio FTP especificado a "ftpuser":
```
chown -R ftpuser:ftpgroup /root/ftphome
```

### Reinicar servidor FTP (usar también para iniciar):
```
/etc/init.d/pure-ftpd restart
```

### Obtener dirección IP del contenedor generado:
```
docker inspect ftp_server | grep "IPAddress"
```



## Docker (Cliente FTP)

### Crear imagen de Docker del cliente FTP:
```
docker build -t curl -f ~/Documents/client.Dockerfile .
```

### Ejecutar el contenedor en modo interactivo:
```
docker run -it --privileged --name ftp_client curl
```

## Comandos usados en el cliente FTP (Curl)

### Subir archivo al servidor FTP:
```
curl -T myfile.txt -u "john_doe:123" ftp://172.17.0.2/
```
`-T [archivo]` indica el archivo (o su ubicación) a subir.

### Descargar archivo del servidor FTP:
```
curl -u "john_doe:123" -O ftp://172.17.0.2/img.png
```

### Listar archivos en el servidor FTP:
```
curl -u "john_doe:123" ftp://172.17.0.2/
```
`-u "[usuario]:[contraseña]` indica las credenciales del usuario para iniciar sesión en el servidor FTP.
`ftp://[IP]/` indica la dirección IP/dominio al servidor FTP a conectar.