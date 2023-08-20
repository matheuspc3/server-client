import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Conexão aceita por: {client_address}")
    
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Mensagem recebida de {client_address}: {message.upper()}")
    
    response = f"Serviço feito pela thread: {threading.current_thread().name}"
    client_socket.send(response.encode('utf-8'))
    
    client_socket.close()
    print(f"Conexão com {client_address} desfeita")

def main():
    host = '127.0.0.1'
    port = 12345
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    
    print(f"Server escutado pelo {host}:{port}")
    
    while True:
        client_socket, client_address = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    main()
