import socket

addresses = {
    "google": "https://www.google.com",
    "test": "https://www.test.com",
    "svsu": "https://www.svsu.edu/"
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 9998))
server_socket.listen(1)
print("Server running on port 9998...")

client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

while True:
    data = client_socket.recv(1024).decode().strip()
    if not data:
        break

    if data.lower() == 'exit':
        print("Client requested disconnect.")
        break

    print(f"Client: {data}")

    key = data.lower()
    if key in addresses:
        response = f"{addresses[key]}"
    else:
        response = f"No record found for '{data}'."

    client_socket.send(response.encode())
    print(f"Response: {response}")

client_socket.close()
server_socket.close()
print("Server closed.")
