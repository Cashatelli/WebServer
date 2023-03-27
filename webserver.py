import socket


def main():
    server_ip = '127.0.0.1'
    server_port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print(f'Server is running on {server_ip}:{server_port}')

    while True:
        connection_socket, client_address = server_socket.accept()
        print(f'Connection from {client_address}')

        request = connection_socket.recv(1024).decode()
        file_path = request.split()[1][1:]

        try:
            with open(file_path, 'r') as file:
                content = file.read()
                response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(content)}\r\nContent-Type: text/html\r\n\r\n{content}"
        except FileNotFoundError:
            response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\nFile not found."

        connection_socket.send(response.encode())
        connection_socket.close()
if __name__ == '__main__':
    main()