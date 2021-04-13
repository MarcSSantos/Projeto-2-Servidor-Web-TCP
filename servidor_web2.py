from socket import *
import datetime
import platform
import mimetypes
import os
###############################################
# Digita na URL do navegador -> localhost:8080
###############################################
plataforma = platform.system().title()

if plataforma != 'Windows':
   os.chdir('C:/Users/marcs/Documents/Redes/pro/Projeto-2-Servidor-Web-TCP')
else:
    os.chdir('C:\\Users\\marcs\\Documents\\Redes\\pro\\Projeto-2-Servidor-Web-TCP')
    
diretorio_atual = os.getcwd()
print(diretorio_atual)
lista_de_arquivos = os.listdir(path=diretorio_atual)

def servidorWebSimples():
    socket_servidor = socket(AF_INET, SOCK_STREAM)
    porta = 8080
    host = 'localhost'

    try:
        socket_servidor.bind((host, porta))  # (('localhost',8080))
        socket_servidor.listen()
        print(f'Aguardando requisições...')

        while True:
            print('quase lá')
            socket_cliente, endereco_cliente = socket_servidor.accept()
            print(f'Conexão estabelecida com o endereço: {endereco_cliente}')

            requisicao = socket_cliente.recv(1024).decode()
            print(requisicao)
            dados_do_cabecalho = requisicao.split('\n')
            print(dados_do_cabecalho)
            arquivo_requisitado = dados_do_cabecalho[0].split()[1].replace('/', '\\')

            #-- Identificando a plataforma
            sistema = platform.system()
            versao_sistema = platform.release()
            #--

            #-- Formatando a data
            formatacao = '%a, %d %b %Y %H:%M:%S'

            dia_atual = datetime.datetime.today()

            data_e_horario = dia_atual.now().strftime(formatacao)
            #--

            print(f'Reequisição do arquivo do arquivo mazelado {arquivo_requisitado}\n\n')

            #mensagem = ''
            print(os.getcwd()+arquivo_requisitado)
            cabecalho = ('HTTP/1.1 200 OK'
                         'Server: Local Teste'
                         'System: sistema versao_sistema'
                         'Content-Type: text/html; charset=utf-8'
                         'Date: Wed, 07 Sep 2016 00:11:31 GMT'
                         'Connection: Keep-alive'
                         'Allow: GET'

                         'Content-Length: 41823')

            if arquivo_requisitado == '\\':

                mensagem = (b'HTTP/1.1 200 OK'
                            b'\r\nServer: Local Teste'
                            b'\r\nSystem: ' + sistema.encode() + b' ' + versao_sistema.encode() +
                            b'\r\nDate: ' + data_e_horario.encode() + b' UTC'
                            b'\r\nContent-Type: text/html; charset=utf-8\r\n\r\n')
                #f'<link rel="icon" href="#">\r\n'
                  
                mensagem += ('<!DOCTYPE html>'
                             '\r\n<html lang="pt-br">'
                             '\r\n<head>'
                             '\r\n<title>Olá, essa e uma página de testes</title>'
                             '\r\n</head>'
                             '\r\n<body>'
                             '\r\n<h1>Lista de arquivos</h1>'
                             '\r\n<table boder="1">'
                             '\r\n<tr>'
                             '\r\n<td> <h2 style = "text-align: left";>Arquivos<h2> </td>'
                             '\r\n<td> <h2 style ="margin-right: 50px; text-align: center;">Bites<h2> </td>'
                             '\r\n<td> <h2 style = "text-align: center";>Data/Hora<h2> </td>'
                             '\r\n</tr>').encode()


                for arquivo in lista_de_arquivos:
                    bytes_arquivo = (os.path.getsize(arquivo))

                    tamanho_arquivo = f'{bytes_arquivo/1024:.2f} KB' if f'{bytes_arquivo/(1024**2):.2f}' == '0.00' else f'{bytes_arquivo/(1024**2):.2f} MB'

                    mensagem += (f'\r\n<tr>'
                                 f'\r\n<td><h4 style ="margin-right: 50px; text-align: left;"><a href="\\{arquivo}">{arquivo}</a></h4></td>'
                                 f'\r\n<td>{tamanho_arquivo}</td>'
                                 f'\r\n<td>{data_e_horario}</td>'
                                 f'\r\n</tr>').encode()

                mensagem += ('\r\n</table>'
                             '\r\n</body>'
                             '\r\n</html>\r\n').encode()

                socket_cliente.send(mensagem)
                socket_cliente.close()

            else:
                try:
                    extensao = mimetypes.MimeTypes().guess_type(os.getcwd()+arquivo_requisitado)[0]

                    caract_escritos = b''

                    if extensao == None:
                        extensao = "text/txt"

                    arquivo = open(os.getcwd()+arquivo_requisitado, 'rb')
                    leitura_arquivo = arquivo.readlines()

                    for char in leitura_arquivo:
                        caract_escritos += char

                    #print('começando...\n', text.decode())
                    bits = str(len(caract_escritos))

                    mensagem = (b'HTTP/1.1 200 OK'
                                b'\r\nServer: Local Teste'
                                b'\r\nSystem: ' + sistema.encode() + versao_sistema.encode() +
                                b'\r\nDate: ' + data_e_horario.encode() + b' UTC'
                                b'\r\n' + dados_do_cabecalho[2].encode() +
                                b'\r\nAllow: ' + dados_do_cabecalho[0].split()[0].encode() +
                                b'\r\nContent-Length: ' + bits.encode() +
                                b'\r\nContent-Type: ' + extensao.encode() + b'; charset=utf-8\r\n\r\n')

                    mensagem += caract_escritos

                    if extensao.split('/')[0] == 'text':
                        print(mensagem.decode())

                    socket_cliente.send(mensagem)
                    socket_cliente.close()

                except FileNotFoundError:
                    mensagem = (b'HTTP/1.1 404 Not Found'
                                b'\r\nServer: Local Teste'
                                b'\r\nSystem: ' + sistema.encode() + b' ' + versao_sistema.encode() +
                                b'\r\nDate: ' + data_e_horario.encode() + b' UTC'
                                b'\r\nContent-Type: text/html; charset=utf-8\r\n\r\n')

                    mensagem += (b'<!DOCTYPE html>'
                                 b'\r\n<html lang="pt-br">'
                                 b'\r\n<head>'
                                 b'\r\n<meta charset = "UTF-8">'
                                 b'\r\n<title>Ola, essa e uma pagina de testes</title>'
                                 b'\r\n</head>'
                                 b'\r\n<body>'
                                 b'\r\n<h1>HTTP/1.1 404 NOT FOUND</h1>'
                                 b'\r\n<h3>File Not Found</h3>'
                                 b'\r\n</body>'
                                 b'\r\n</html>\r\n')

                    print(mensagem.decode())
                    socket_cliente.send(mensagem)
                    socket_cliente.close()

            #print(f'Começando...\n{mensagem}')

    except KeyboardInterrupt:
        print('Encerrando...')

    except Exception as exc:
        print(f'Erro: {Exception}{exc}')

    socket_servidor.close()

servidorWebSimples()
