# SocketShell - For Command Execution

## Overview

This command execution tool allows for remote command execution between two machines, similar to tools like Netcat or SSH. It consists of two components: a server and a client. The server listens for incoming connections from clients, while the client connects to the server and server sends commands for execution.

## Features

- **Server Component:** Listens for incoming connections from client and sends commands to the client.
- **Client Component:** Connects to the server and execute commands received from the server.
- **Command Execution:** Allows users to execute commands on the client remotely from the server.
- **Support for Sudo:** Provides functionality to execute commands with sudo privileges.

## Usage

### Setting up the Server

1. Ensure Python 3 is installed on your server machine.
2. Copy and paste the server script (`server.py`) to your server machine.
3. Specify the IP address and port according to your requirements in the script.
4. Run the server script using the command:

   ```bash
   python3 server.py
5. Once connected, you can start sending commands to the client.

### Connecting from the Client

1. Ensure Python 3 is installed on your client machine.
2. Copy and paste the client script (`client.py`) to your client machine.
3. Specify the IP address and port according to your requirements in the script.
4. Run the client script using the command:

   ```bash
   python3 client.py


## Example Commands

- **Execute a Command:**
  To execute a command on the client from the server, simply type the command after establishing the connection.

- **Exit:**
  To exit the Both Sides, type `exit`.

- **Sudo Command:**
  If executing a command with sudo privileges, the server will prompt for the root password.

## Security Considerations

- Ensure firewall settings allow connections on the specified port `8888`.
- Implement authentication mechanisms if deploying in production environments.
- Use responsibly and avoid deploying in production environments without proper security measures.

## Author

[DeaDDroid](https://github.com/DeadDroid401)

## Contributions

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).



