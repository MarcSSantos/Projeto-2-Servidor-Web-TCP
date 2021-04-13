from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread



class Dados:
    def __init__(self, sock):
        dados = sock.recv(1024)
        print(f'Resposta do servidor: \n{dados.decode()}')
        

class Cliente:
    def __init__(self, endereco, porta):
        sock = socket(AF_INET, SOCK_STREAM)
        print('Aguardando conexão...')
        
        sock.connect((endereco, porta))
        print('Conexão realizada.')
        print(f'{sock}')
         
        Thread(target=Dados, args=(sock,)).start()

        mensagem = input('Peça o arquivo: ')
        sock.send(mensagem.encode())


cliente_tcp = Cliente('localhost', 8080)