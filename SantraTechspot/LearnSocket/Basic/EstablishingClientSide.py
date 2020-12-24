#

import socket

# Step 1 : Craete Socket object
s = socket.socket()

# Setp 2 : Set Host_name and Port

host = socket.gethostname()
port = 1234

# Step 3 : Connection establishing

    # host and port passes in tuple format , I think tuple is immutable so we pass in tuple
s.connect((host, port))
    # recv is receving the message form server and buffer Size
print(s.recv(1024))