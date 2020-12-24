import time, socket, sys
print("\n\t =====> Welcome to Chat Room <===== ")
print("\n \t Intialising....... ")
time.sleep(1)
s = socket.socket()

host = socket.gethostname()
ip = socket.gethostbyname(host)  # Return a IP address in String format
# Given a input host because in this host name have some ip address
port = 1234
s.bind((host, port))

print(f"Host : {host} and IP : {ip}")
S_name = str(input("Enter your name : "))
s.listen(1)

print("\n\t Waiting for incoming  Connection .....")
conn, addr = s.accept()
print(f"\n Recevied Connection from address : {addr[0]} port no :{addr[1]}")

C_name = conn.recv(1024)
C_name=C_name.decode()  # Recevie the client name in Bit code convert to String Code
print(f"{C_name} has connected to Chart Room ")

# Sent my name to Client in encode
conn.send(S_name.encode())

# <=========  Chat Process =========>

while True:
    # Sent Message
    s_message = input(str(f"{S_name} : "))
    conn.send(s_message.encode())
    # Reacive Message
    r_message = conn.recv(1024)
    r_message = r_message.decode()
    print(f"{C_name} : {r_message}")
    if s_message == "bye" or s_message == "Bye" or s_message == "q" :
        break
