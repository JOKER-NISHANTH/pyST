# TCP 
# 1-Server_Side_Script
import socket

# Step 1 : Create thee socket
s = socket.socket()

# Setp 2 : First we need a host and ports details to create communication
host =socket.gethostname()  # gethostname() ==> returns crt ip address
port = 1234

# Step 3 : Binding
s.bind((host,port))

# Step 4 : Server Lisenting any client connected ah
s.listen(5)

# Step 5: Connection  Accepting
while True:
    connection, ip_address = s.accept()
    print(f"Got connection from : {ip_address}")

    # Sent some greeting for connected person in byte format
    connection.send(b'Thank you for connecting ')
    connection.close()
