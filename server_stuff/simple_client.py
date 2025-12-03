import socket
port,host = 9998, '0.0.0.0'
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
except (ConnectionRefusedError, TimeoutError, OSError):
    print("Error: Could not connect to the server.")
    exit(1)
while True:
    message_to_server = input("You: ")
    if message_to_server == 'exit':
        break
    client_socket.send(message_to_server.encode())
    response_from_server = client_socket.recv(1023).decode()
    print(f"Server: {response_from_server}")
client_socket.close()