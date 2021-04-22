from socket import *
import datetime
import platform
import mimetypes
import os
import time
###############################################
# Digita na URL do navegador -> localhost:8080
###############################################
plataforma = platform.system().title()

#if plataforma != 'Windows':
#    os.chdir('/c/Projeto_servidor_web/arq')
#else:
#    os.chdir('C:\\Projeto_servidor_web\\arq')
def verifica_diretorio_ex():
    caminho_inicial = ''
    
    if plataforma == "Windows":
        caminho_inicial = os.getcwd()+'\\arq'
    
    else:
        caminho_inicial = os.getcwd()+'/arq'
        
    try:
        os.listdir(caminho_inicial)
        
    except:
        
        os.mkdir(caminho_inicial)
          

def join_method(lista):
  return ''.join(['\\'+x if x != lista[0] else x for x in lista])


def pop_dir(diretorio):
    # C:\Projeto_servidor_web\arq\omega
    restringir = diretorio.split('\\')
    
    if restringir[-1] != 'arq':
        restringir.pop()
        return restringir
    
    else:
        return restringir
        
    

def servidorWebSimples():
    socket_servidor = socket(AF_INET, SOCK_STREAM)
    porta = 8080
    host = 'localhost'

    try:
        socket_servidor.bind((host, porta))  # (('localhost',8080))
        socket_servidor.listen()
        
        verifica_diretorio_ex()
        
        print(f'Aguardando requisições...')
        
        diretorio_primario = os.getcwd() + '\\arq' #pasta onde deve ficar os arquivos não intrinsecos ao servidor
        
        diretorio_atual = diretorio_primario
        
        #-- Identificando a plataforma
        sistema = platform.system()
        versao_sistema = platform.release()
        
#-----------------------------------------------------------------------------------------------------------------------------        
        while True:
            socket_cliente, endereco_cliente = socket_servidor.accept()
            print(f'\nConexão estabelecida com o endereço: {endereco_cliente}')
            
            requisicao = socket_cliente.recv(1024).decode()
            dados_do_cabecalho = requisicao.split('\n')
            
            arquivo_nao_tratado = dados_do_cabecalho[0].split()[1].replace('/', '\\') if len(requisicao) != 0 else '/' if plataforma != 'Windows' else '\\' 
            arquivo_requisitado = arquivo_nao_tratado.replace('%20',' ') if '%20' in arquivo_nao_tratado else arquivo_nao_tratado

            lista_arquivos_sem_permissao = os.listdir(os.getcwd())
            
            lista_de_caminhos = (diretorio_atual).split('\\')
            for elem in range(2, len(diretorio_atual.split('\\'))):#####[::-1]:

                
                if arquivo_requisitado != '\\' and arquivo_requisitado[1:] not in lista_arquivos_sem_permissao:
                    aux = os.listdir(diretorio_atual) if not os.path.isfile(diretorio_atual+arquivo_requisitado) else ''
                    
                    #if lista_de_caminhos[elem] == 'arq' and arquivo_requisitado[1:] not in aux:
                    #    raise FileNotFoundError
                    
                    if arquivo_requisitado[1:] == lista_de_caminhos[elem]:
                        diretorio_atual = join_method(lista_de_caminhos[0:elem])
                        break                 

                                     
                    elif aux != '' and arquivo_requisitado[1:] in aux: # SE O ARQUIVO ESTIVER, o diretório atual vai ter que ser reconstruídoooooooooo
                        diretorio_atual += arquivo_requisitado
                        break
                       
                    #elif aux != '' and arquivo_requisitado[1:] not in aux:
                        #separa_dir = pop_dir(diretorio_atual)
                        #junta_dir = join_method(separa_dir[elem+1:]) #Vai pegar a todas as pastas a partir da solicitação. Ex.: Solicito aquivo de uma pasta anterior, então ele vai apagar a pasta atual e vai retroceder
                        #novo_dir = diretorio_atual.replace('\\'+junta_dir,'') #Substitui o diretório antigo, pelo o novo
                        #diretorio_atual = novo_dir
                        #print(diretorio_atual, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA 2')
                        #break
                        
                #-----------------------------------------------------------------------------    
                #SE FOR SÓ BARRAAAAAAAAAAAAAA, EU NÃO ADICIONOOOOOOOOOOOOOOOOOOOOOOOOOO      |
                #-----------------------------------------------------------------------------    
                else:
                    break
                

            #-- Formatando a data
            formatacao = '%a, %d %b %Y %H:%M:%S'
            dia_atual = datetime.datetime.today()
            data_e_horario = dia_atual.now().strftime(formatacao)
            #--
                
            print(f'Reequisição do arquivo -> {arquivo_requisitado}\n\n')


            print('Buscando... ', diretorio_atual+' + '+arquivo_requisitado)
            
            cabecalho = ('HTTP/1.1 200 OK'
                         'Server: Local Teste'
                         'System: sistema versao_sistema'
                         'Content-Type: text/html; charset=utf-8'
                         'Date: Wed, 07 Sep 2016 00:11:31 GMT'
                         'Connection: Keep-alive'
                         'Allow: GET'

                         'Content-Length: 41823')


            arquivo_v = os.path.isfile(diretorio_atual+arquivo_requisitado)
            
            if arquivo_requisitado[-1] == '\\' or arquivo_v == False and arquivo_requisitado[1:] not in lista_arquivos_sem_permissao:
                
                #else:
                #                   
                #    diretorio_atual += arquivo_requisitado if arquivo_requisitado != '\\' else ''
                #    print(diretorio_atual, 'BANADAAAAAAAAAAAAAAAAAAAAAAAAAA 3')

                mensagem = (b'HTTP/1.1 200 OK'
                            b'\r\nServer: Local Teste'
                            b'\r\nSystem: ' + sistema.encode() + b' ' + versao_sistema.encode() +
                            b'\r\nDate: ' + data_e_horario.encode() + b' UTC'
                            b'\r\nContent-Type: text/html; charset=utf-8\r\n\r\n')
                

                voltar = diretorio_atual.split("\\")[-1] if diretorio_atual.split("\\")[-1] != 'arq' else ''

                mensagem += (f'<!DOCTYPE html>'
                             f'\r\n<html lang="pt-br">'
                             f'\r\n<head>'
                             f'\r\n<meta name = "viewport" content = "width=device-wwidth, initial-scale=1.0">'
                             f'\r\n<title>Olá, essa e uma página de testes</title>'
                             f'\r\n<link rel="icon" type="image/x-icon" href="favicon.ico">'
                             f'\r\n<link rel="stylesheet" href="./styleProjRedes.css">'
                             f'\r\n</head>'
                             f'\r\n<body>'
                             f'\r\n<nav class>'
                             f'\r\n<a href="\\"><input type="submit" value="Atualizar lista de arquivos" class = "atualizar"></a>'
                             f'\r\n<a href="\\{voltar}"><input type="submit" value="Voltar Pasta" class = "voltar"></a>'
                             f'\r\n</nav>'
                             f'\r\n<nav>'
                             f'\r\n<table class="tabela">'
                             f'\r\n<thead class="nome_coluna">'
                             f'\r\n<tr>'
                             f'\r\n<td>Arquivos</td>'
                             f'\r\n<td>Bites</td>'
                             f'\r\n<td>Data/Hora</td>'
                             f'\r\n</tr>'
                             f'\r\n</thead>'
                             f'\r\n<tbody class="arquivo">').encode()

                
                lista_de_arquivos = os.listdir(path=diretorio_atual)
                
                for arquivo in lista_de_arquivos:
                    verifica_pasta = 'PASTA' if not os.path.isfile(diretorio_atual+'\\'+arquivo) else 'ABACATE'

                    modificacao = os.path.getmtime(diretorio_atual+'\\'+arquivo)
                    modificacao_local = time.ctime(modificacao)

                    if verifica_pasta == 'PASTA':
                        bytes_pasta = sum([os.path.getsize(diretorio_atual+'\\'+arquivo+'\\'+f) for f in os.listdir(diretorio_atual+'\\'+arquivo)])

                        tamanho_pasta = f'{bytes_pasta/1024:.2f} KB' if f'{bytes_pasta/(1024**2):.2f}' == '0.00' else f'{bytes_pasta/(1024**2):.2f} MB'

                        mensagem += (f'\r\n<tr>'
                                    f'\r\n<td><h4><a href="\\{arquivo}" class="link_arq">{arquivo}\\.</a></h4></td>'
                                    f'\r\n<td>{tamanho_pasta}</td>'
                                    f'\r\n<td>{modificacao_local}</td>'
                                    f'\r\n</tr>').encode()

                    else:
                        bytes_arquivo = (os.path.getsize(diretorio_atual+'\\'+arquivo))

                        tamanho_arquivo = f'{bytes_arquivo/1024:.2f} KB' if f'{bytes_arquivo/(1024**2):.2f}' == '0.00' else f'{bytes_arquivo/(1024**2):.2f} MB'

                        mensagem += (f'\r\n<tr>'
                                    f'\r\n<td><h4><a href="\\{arquivo}" class="link_arq">{arquivo}</a></h4></td>'
                                    f'\r\n<td>{tamanho_arquivo}</td>'
                                    f'\r\n<td>{modificacao_local}</td>'
                                    f'\r\n</tr>').encode()

                mensagem+= ('\r\n</tbody>'
                            '\r\n</table>'
                            '\r\n</nav>'
                            '\r\n</body>'
                            '\r\n</html>\r\n').encode()

                socket_cliente.send(mensagem)
                #socket_cliente.close()               
#----------------------------------------------------------------------------------------------------------------------
#Falta leeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeer
            else:
                try:                    
                    leitura_arquivo = ''
                    if arquivo_requisitado == '\\styleProjRedes.css' or arquivo_requisitado == '\\favicon.ico':
                        with open(os.getcwd()+arquivo_requisitado, 'rb') as arquivo:
                            leitura_arquivo = arquivo.readlines()
                            
                        extensao = mimetypes.MimeTypes().guess_type(os.getcwd()+arquivo_requisitado)[0]
                    
                    else:
                        with open(diretorio_atual+arquivo_requisitado, 'rb') as arquivo:
                            leitura_arquivo = arquivo.readlines()  
                                                             
                        extensao = mimetypes.MimeTypes().guess_type(diretorio_atual+arquivo_requisitado)[0]
                        print(extensao)

                    caract_escritos = b''

                    if extensao == None:
                        extensao = "text/txt"
                

                    for char in leitura_arquivo:
                        caract_escritos += char
                    
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
                        #print(mensagem.decode())
                        pass

                    socket_cliente.send(mensagem)
                    #socket_cliente.close()
                    
                    print(diretorio_atual, '<--')
                    print('-'*50)
                    
                except FileNotFoundError:
                    mensagem = (b'HTTP/1.1 404 Not Found'
                                b'\r\nServer: Local Teste'
                                b'\r\nSystem: ' + sistema.encode() + b' ' + versao_sistema.encode() +
                                b'\r\nDate: ' + data_e_horario.encode() + b' UTC'
                                b'\r\nContent-Type: text/html; charset=utf-8\r\n\r\n')

                    mensagem += ('<!DOCTYPE html>'
                                 '\r\n<html lang="pt-br">'
                                 '\r\n<head>'
                                 '\r\n<title>Olá, essa é uma página de testes</title>'
                                 '\r\n<link rel="icon" type="image/x-icon" href="favicon.ico">'
                                 '\r\n</head>'
                                 '\r\n<body>'
                                 '\r\n<h1>HTTP/1.1 404 NOT FOUND</h1>'
                                 '\r\n<h3>File Not Found</h3>'
                                 '\r\n</body>'
                                 '\r\n</html>\r\n').encode()

                    #print(mensagem.decode())
                    socket_cliente.send(mensagem)
                    socket_cliente.close()
                    
            socket_cliente.close()

    except KeyboardInterrupt:
        print('Encerrando...')

    #except Exception as exc:
    #    print(f'Erro: {Exception}{exc}')

    socket_servidor.close()

servidorWebSimples()

#ADICIONAR ELEMENTO A URL 
#incitar erro notfound caso o arquivo não seja encontrado
#entregar o endereçamento da URL por inteiro, exemplo, quero ir pra pasta nova, então entrego /omega/pasta nova e não só pasta nova

#requisição de volta = #
#criar pasta assim que se inicia o programa