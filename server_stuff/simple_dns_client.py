import socket
import os
import webbrowser

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('0.0.0.0', 9998))

# send
while True:
    message = input("You: ")
    if message == 'exit':
        client_socket.close()

    client_socket.send(message.encode())
    server = client_socket.recv(1023).decode()

    if server =='':
        message = input("You: ")
        client_socket.send(message.encode())
        server = client_socket.recv(1023).decode()
    
    if server == "https://www.google.com":
        url = server
        webbrowser.open_new_tab(url)
    
    if server == "https://www.svsu.edu/":
        url = server
        webbrowser.open_new_tab(url)
    
    else:
        print(f"Server: {server}")
