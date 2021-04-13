import socket
import os

def handle_request(request):
    """Handles the HTTP request."""
    os.chdir('C:\\Projeto_servidor_web\\arq')
    headers = request.split('\n')
    #print(headers,'TO AQUIIIIIIIIIIIIIIIIIIIII')
    filename = headers[0].split()[1]
    print(filename, 'olha issso aqquiiiiiiiiiiiiiiiiiii')
    if filename == '/':
        filename = 'C:\\Projeto_servidor_web\\arq\\caminho_critico_projeto-ProvaPGP.png'

    try:
        fin = open(filename, 'wb')
        content = fin.read()
        fin.close()
        print(content,'JUBAAAAAAAAAAAAAAAAA')

        response = 'HTTP/1.0 200 OK\n\n' + content
        print(response, 'De LEãaaaaaaaaaaaaaaao')
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    return response


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request,'OEHOOOOOOOOOOOOOOOOOO')

    # Return an HTTP response
    response = handle_request(request)
    client_connection.sendall(response.encode())

    # Close connection
    client_connection.close()

# Close socket
server_socket.close()