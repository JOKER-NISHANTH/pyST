import sys, time, socket
print("\n\t =====> Welcome to Chat Room <===== ")
print("\n Initialising....")
time.sleep(1)

s = socket.socket()
c_host = socket.gethostname()
c_ip = socket.gethostbyname(c_host)
c_port = 1234
print(f" Host : {c_host} and IP address: {c_ip}")

host = input(str("Enter the server address to connect : "))
c_name = input(str("Enter your name : "))

print(f"\n\t Trying to connect {host} ")
time.sleep(1)

s.connect((c_host, c_port))
print("Connected.....\n")

s.send(c_name.encode())

server_name = s.recv(1024)
server_name = server_name.decode()
print(f"{server_name} has joined the chat room ")

while True:
    # Reveive message
    r_message = s.recv(1024)
    r_message = r_message.decode()
    print(f"{server_name} : {r_message}")
    # Send message
    s_message = input(str(f"{c_name} : "))
    s_message = s_message.encode()
    s.send(s_message)
    if s_message == "bye" or s_message == "Bye" or s_message == "q":

        break
