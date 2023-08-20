import socket

def main():
    host = '127.0.0.1'
    port = 12345
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    message = "Essa mensagem é do cliente"
    #message = input("Essa mensagem será enviada para o servidor, escreva com carinho: ")
    client.send(message.encode('utf-8'))
    
    response = client.recv(1024).decode('utf-8')
    print(f"Resposta recebida pelo server: {response}")
    
    client.close()

if __name__ == "__main__":
    main()
