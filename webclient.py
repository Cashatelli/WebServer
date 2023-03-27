import socket

def main():
    server_ip = input("Enter the server IP address: ")
    server_port = int(input("Enter the server port number: "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    file_path = input("Enter the file path: ")
    request = f"GET /{file_path} HTTP/1.1\r\nHost: {server_ip}:{server_port}\r\n\r\n"
    client_socket.send(request.encode())

    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()

if __name__ == '__main__':
    main()
