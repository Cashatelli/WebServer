# WebServer
## Description 
This project implements a simple Python web server that handles one HTTP request at a time. The server accepts and parses an HTTP request, retrieves the requested file from the server's file system, creates an HTTP response message consisting of the requested file, and sends the response directly to the client. If the requested file is not present in the server, the server sends an HTTP "404 Not Found" message back to the client.
## Files
The repository contains the following files:

### server.py:
This is the Python script that implements the web server. It creates a server socket using TCP, listens for incoming connections from a client, extracts the requested file from the message, opens the file to read its contents, and sends an HTTP response message to the client.

### client.py:
This is a Python script that acts as a simple HTTP client. It connects to the server using a TCP connection, sends a request to the server containing the file path of the file to retrieve, receives the server response and contents of the file, and then displays them as output.

### example.html: 
This is a sample HTML file that is used to test the web server.

## Usage
To run the program, follow these steps:

1. Download the files and save them in the same directory.
2. Open a terminal window and navigate to the directory where the files are saved.
3. In one terminal window, run the server by typing python server.py and pressing Enter.
4. In another terminal window, run the client by typing python client.py and pressing Enter.
5. Follow the prompts to enter the IP address and port number of the server, and the file path of the file to retrieve.
6. The server should send the contents of the requested file to the client, and the client should display them as output.

## Contribute!
Please feel free to modify the code to suit your specific requirements or use it as a starting point for your own projects.
