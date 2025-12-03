import socket
port, host = 9998, '0.0.0.0'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print("Server is listening on port 9999...")

client_socket, client_address = server_socket.accept()

print(f"Connected to {client_address}")

try:
    while True:
        client = client_socket.recv(1023).decode()
        
        if client == '' or client == 'exit':
            break
        print(f"Client says: {client}")
        response_to_client = "test"
        client_socket.send(response_to_client.encode())
        print(f"Response: {response_to_client}")
except (BrokenPipeError, ConnectionResetError):
    print(f"Client disconnected")
finally:
    client_socket.close()