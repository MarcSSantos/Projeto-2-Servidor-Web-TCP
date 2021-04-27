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

def verifica_diretorio_ex():
    '''
    Verifica se há uma pasta para armazenar os arquivos do servidor
    caso não haja qualquer pasta, cria um novo diretório para armazenar
    os arquivos do servidor
    '''
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
    '''
    Método para acelerar e facilitar a junção 
    dos elementos de uma lista de diretórios
    '''
    indicador_de_caminho = '\\'
    
    if plataforma != 'Windows':
        indicador_de_caminho = '/'
    
    return ''.join([indicador_de_caminho+x if x != lista[0] else x for x in lista])


def pop_dir(diretorio):
    '''
    Vai reduzindo um diretório a cada vez que é chamada a função
    '''
    
    indicador_de_caminho = '\\'
    
    if plataforma != 'Windows':
        indicador_de_caminho = '/'
        
    # C:\Projeto_servidor_web\arq\omega
    restringir = diretorio.split(indicador_de_caminho)
    
    if restringir[-1] != 'arq':
        restringir.pop()
        return restringir
    
    
    else:
        return restringir
    

def erros_requisicao(get):
    '''
    Verifica a integridade do GET, se houver alguma discrepância,
    a função retorna com uma mensagem de erro, caso contrário,
    retorna uma mensagem que não encontrou nenhum erro.
    '''
    try:
        msg_erro = ''
        erro = True
                   
        if get[0] != 'GET' or get[2][:4] != 'HTTP':
            msg_erro = ('HTTP/1.1 400 BAD REQUEST\r\n'
                        'Content-Type: text/html\r\n'
                        'charset=utf-8 \r\n\r\n'
                        '<!DOCTYPE html>'
                        '\r\n<html lang="pt-br">'
                        '\r\n<head>'
                        '\r\n<meta charset="UTF-8">'
                        '\r\n<meta name="viewport" content="width=device-width, initial-scale=1.0">'
                        '\r\n<title>Olá, essa e uma página de testes</title>'
                        '\r\n<link rel="icon" type="image/x-icon" href="favicon.ico">'
                        '\r\n</head>'
                        '\r\n<body>'
                        '\r\n<h1>400 BAD REQUEST</h1>'
                        '\r\n</body>'
                        '\r\n</html>\r\n').encode()
            
        elif get[2][5:] != "1.1":
            msg_erro = ('HTTP/1.1 505 HTTP Version Not Supported\r\n'
                        'Content-Type: text/html\r\n'
                        'charset=utf-8 \r\n\r\n'
                        '<!DOCTYPE html>'
                        '\r\n<html lang="pt-br">'
                        '\r\n<head>'
                        '\r\n<meta charset="UTF-8">'
                        '\r\n<meta name="viewport" content="width=device-width, initial-scale=1.0">'
                        '\r\n<title>Olá, essa e uma página de testes</title>'
                        '\r\n<link rel="icon" type="image/x-icon" href="favicon.ico">'
                        '\r\n</head>'
                        '\r\n<body>'
                        '\r\n<h1>505 HTTP Version Not</h1>'
                        '\r\n</body>'
                        '\r\n</html>\r\n').encode()
            
        else:
            erro = False
            return msg_erro, erro
    
    except:
        msg_erro = ('HTTP/1.1 400 BAD REQUEST\r\n'
                    'Content-Type: text/html\r\n'
                    'charset=utf-8 \r\n\r\n'
                    '<!DOCTYPE html>'
                    '\r\n<html lang="pt-br">'
                    '\r\n<head>'
                    '\r\n<meta charset="UTF-8">'
                    '\r\n<meta name="viewport" content="width=device-width, initial-scale=1.0">'
                    '\r\n<title>Olá, essa e uma página de testes</title>'
                    '\r\n<link rel="icon" type="image/x-icon" href="favicon.ico">'
                    '\r\n</head>'
                    '\r\n<body>'
                    '\r\n<h1>400 BAD REQUEST</h1>'
                    '\r\n</body>'
                    '\r\n</html>\r\n').encode()
        
    return msg_erro, erro
            

def atualiza_dir(diratual, requisicao, dplataforma):
    '''
    Essa função serve para atualizar um diretório de acordo com a requisição que foi realizada
    '''
    #diretorio = diratual
    arqrequisitado = requisicao
    divisor_caminho = dplataforma
    j = arqrequisitado.split(divisor_caminho) if arqrequisitado != divisor_caminho else ['','']
    diretorio = diratual#os.getcwd()+divisor_caminho+'arq'+divisor_caminho.join(j[:-2])
    print(diretorio,'AAAAAAAAAAAAAAAAA', arqrequisitado)
    
    arquivos_sem_permissao = os.listdir(os.getcwd())
    
    lista_de_caminhos = diretorio.split(divisor_caminho)

    if arqrequisitado[1:] == lista_de_caminhos[-1]:
        if arqrequisitado[1:] in os.listdir(diretorio):
            return diretorio + arqrequisitado 
        
        else:
            return diretorio  
    
    for _ in range(lista_de_caminhos.index('arq'), len(lista_de_caminhos)):

        if arqrequisitado != divisor_caminho and arqrequisitado[1:] not in arquivos_sem_permissao:
            aux = os.listdir(diretorio) if not os.path.isfile(diretorio+arqrequisitado) else ''
                                              
            if aux != '' and arqrequisitado[1:] in aux: # SE O ARQUIVO ESTIVER, o diretório atual vai ter que ser reconstruídoooooooooo
                diretorio += arqrequisitado
                break          
            
            elif aux != '' and arqrequisitado[1:] not in aux and arqrequisitado[1:] != 'voltar':
                separa_dir = pop_dir(diretorio)
                                              
                junta_dir = join_method(separa_dir) #Vai pegar a todas as pastas a partir da solicitação. Ex.: Solicito aquivo de uma pasta anterior, então ele vai apagar a pasta atual e vai retroceder
                diretorio = junta_dir
            
                if separa_dir[-1] == 'arq':
                    ultimo_dir = os.listdir(junta_dir)
                                        
                    if arqrequisitado[1:] not in ultimo_dir:                        
                        raise FileNotFoundError
                                        
    return diretorio
    

def servidorWebSimples():
    socket_servidor = socket(AF_INET, SOCK_STREAM)
    porta = 8080
    host = 'localhost'
    verifica_diretorio_ex()

    try:
        socket_servidor.bind((host, porta))  # (('localhost',8080))
        socket_servidor.listen()
        
        estabelece_plataforma = '\\' if plataforma == 'Windows' else '/'
        
        print(f'Aguardando requisições...')
        
        diretorio_primario = os.getcwd() + estabelece_plataforma + 'arq' #pasta onde deve ficar os arquivos não intrinsecos ao servidor
        
        diretorio_atual = diretorio_primario
        
        #-- Identificando a plataforma
        sistema = platform.system()
        versao_sistema = platform.release()
        
        lista_arquivos_sem_permissao = os.listdir(os.getcwd())#não valida arquivos que estão junto com o servidor
#-----------------------------------------------------------------------------------------------------------------------------        
        while True:
            socket_cliente, endereco_cliente = socket_servidor.accept()
            print(f'\nConexão estabelecida com o endereço: {endereco_cliente}')
            
            requisicao = socket_cliente.recv(1024).decode()
            dados_do_cabecalho = requisicao.split('\n')
            
#------------------------------------------------------------------------------------------------------------------------------------
            msg, erro_na_requisicao = erros_requisicao(dados_do_cabecalho[0].split())#valida a condição do get

            #Só vai verificar a condição do GET, se houver algum erro, o ciclo abaixo é interrompido e o cliente recebe uma mensagem de error
            if erro_na_requisicao == True:
                socket_cliente.send(msg)
                socket_cliente.close()               
                continue
            
#------------------------------------------------------------------------------------------------------------------------------------            
            #as 2 variáveis logo abaixo só tratam a condição do get, no caso, trata arquivo com espaçamento
            arquivo_nao_tratado = dados_do_cabecalho[0].split()[1].replace('/', estabelece_plataforma) if len(requisicao) != 0 else ''
            zaun = arquivo_nao_tratado.replace(estabelece_plataforma, '#'+estabelece_plataforma)
            b = zaun.split('#')
            
            arquivo_requisitado = b[-1].replace('%20',' ') if '%20' in b[-1] else b[-1]
            print('MISCA MUSCAAAAAAAAAAAAAAA')
            
#------------------------------------------------------------------------------------------------------- 
            if arquivo_requisitado[1:] not in lista_arquivos_sem_permissao:           
                sp = diretorio_atual.split(estabelece_plataforma)
                print(sp)
                jj = estabelece_plataforma+estabelece_plataforma.join(sp[sp.index('arq')+1:])
                print(jj, 'MINIEEEEE')
                kk = ''.join(b)
                print(kk, 'PATETAAAAA')
                st = kk.replace(jj, '') if kk != estabelece_plataforma else ''
                print(st,'PATO DONALDD')
                #st = estabelece_plataforma.join(sp[sp.index('arq')+1:])#posso dar .join
                print(st)  #Vou ter que dar replace nos elementos da requisição que são iguais a meu diretório atual
                print(f'Reequisição do arquivo -> {arquivo_requisitado}\n\n')
#----------------------------------------------------------------------------------------------------------            
            if arquivo_requisitado[1:] == 'voltar':
                voltar = pop_dir(diretorio_atual)
                diretorio_atual = join_method(voltar)
                arquivo_requisitado = estabelece_plataforma#+voltar[-1] if voltar[-1] != 'arq' else "\\"
   

            
            #atualiza o diretório a partir das requisições
            try:
                diretorio_atual = atualiza_dir(diretorio_atual, arquivo_requisitado, estabelece_plataforma) if arquivo_requisitado[1:] not in lista_arquivos_sem_permissao else diretorio_atual
            
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
                            '\r\n<meta name="viewport" content="width=device-width, initial-scale=1.0">'
                            '\r\n<meta charset = "utf-8">'
                            '\r\n</head>'
                            '\r\n<body>'
                            '\r\n<h1>HTTP/1.1 404 NOT FOUND</h1>'
                            '\r\n<h3>File Not Found</h3>'
                            '\r\n</body>'
                            '\r\n</html>\r\n').encode()

                socket_cliente.send(mensagem)
                socket_cliente.close()
                continue

            #-- Formatando a data
            formatacao = '%a, %d %b %Y %H:%M:%S'
            dia_atual = datetime.datetime.today()
            data_e_horario = dia_atual.now().strftime(formatacao)
            #--


            print('Buscando... ', diretorio_atual+' + '+arquivo_requisitado)
            
            #verifica se a requisição é um arquivo ou pasta
            arquivo_v = os.path.isfile(diretorio_atual+arquivo_requisitado)
            
            
            #essa condição serve para verificar se uma requisição é só uma barra ou uma pasta e então listar o diretório
            if arquivo_requisitado[-1] == estabelece_plataforma or arquivo_v == False and arquivo_requisitado[1:] not in lista_arquivos_sem_permissao:

                atualizar = estabelece_plataforma# if diretorio_atual.split('\\')[-1] != 'arq' else ''
                
                
                mensagem = (b'HTTP/1.1 200 OK'
                            b'\r\nServer: Local Teste'
                            b'\r\nSystem: ' + sistema.encode() + b' ' + versao_sistema.encode() +
                            b'\r\nDate: ' + data_e_horario.encode() + b' UTC'
                            b'\r\nContent-Type: text/html; charset=utf-8\r\n\r\n')
                
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
                             f'\r\n<a href="{st}"><input type="submit" value="Atualizar lista de arquivos" class = "atualizar"></a>'
                             f'\r\n<a href="{estabelece_plataforma.join(pop_dir(st))}"><input type="submit" value="Voltar Pasta" class = "voltar"></a>'
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
                
                #esse for serve como uma lista em HTML, apenas para dar propriedades href aos arquivos listados da pasta
                for arquivo in lista_de_arquivos:
                    verifica_pasta = 'PASTA' if not os.path.isfile(diretorio_atual+estabelece_plataforma+arquivo) else 'ABACATE'

                    modificacao = os.path.getmtime(diretorio_atual+estabelece_plataforma+arquivo)
                    modificacao_local = time.ctime(modificacao)

                    if verifica_pasta == 'PASTA':
                        bytes_pasta = sum([os.path.getsize(diretorio_atual+estabelece_plataforma+arquivo+estabelece_plataforma+f) for f in os.listdir(diretorio_atual+estabelece_plataforma+arquivo)])

                        tamanho_pasta = f'{bytes_pasta/1024:.2f} KB' if f'{bytes_pasta/(1024**2):.2f}' == '0.00' else f'{bytes_pasta/(1024**2):.2f} MB'

                        mensagem += (f'\r\n<tr>'
                                    f'\r\n<td><h4><a href="{st+estabelece_plataforma+arquivo}" class="link_arq">{arquivo}\\.</a></h4></td>'
                                    f'\r\n<td>{tamanho_pasta}</td>'
                                    f'\r\n<td>{modificacao_local}</td>'
                                    f'\r\n</tr>').encode()

                    else:
                        bytes_arquivo = (os.path.getsize(diretorio_atual+estabelece_plataforma+arquivo))

                        tamanho_arquivo = f'{bytes_arquivo/1024:.2f} KB' if f'{bytes_arquivo/(1024**2):.2f}' == '0.00' else f'{bytes_arquivo/(1024**2):.2f} MB'

                        mensagem += (f'\r\n<tr>'
                                    f'\r\n<td><h4><a href="{st+estabelece_plataforma+arquivo}" class="link_arq">{arquivo}</a></h4></td>'
                                    f'\r\n<td>{tamanho_arquivo}</td>'
                                    f'\r\n<td>{modificacao_local}</td>'
                                    f'\r\n</tr>').encode()

                mensagem+= ('\r\n</tbody>'
                            '\r\n</table>'
                            '\r\n</nav>'
                            '\r\n</body>'
                            '\r\n</html>\r\n').encode()

                socket_cliente.send(mensagem)              
#----------------------------------------------------------------------------------------------------------------------

            #essa nessa contra condição serve para ler, finalmente, o arquivo que foi requisitado
            else:
                try:                    
                    leitura_arquivo = ''
                    
                    #aqui verifica se a requisição tem alguma propriedade necessária para o servidor, ou seja, algum arquivo que é requisitado pelo próprio servidor
                    if 'styleProjRedes.css' in arquivo_requisitado[1:] or 'favicon.ico' in arquivo_requisitado[1:]:

                        with open(os.getcwd()+arquivo_requisitado, 'rb') as arquivo:
                            leitura_arquivo = arquivo.readlines()
                            
                        extensao = mimetypes.MimeTypes().guess_type(os.getcwd()+arquivo_requisitado)[0]
                    
                    #aqui verifica requisições de arquivos provenientes dos clientes e os lê
                    else:
                        with open(diretorio_atual+arquivo_requisitado, 'rb') as arquivo:
                            leitura_arquivo = arquivo.readlines()  
                                                             
                        extensao = mimetypes.MimeTypes().guess_type(diretorio_atual+arquivo_requisitado)[0]
                        print(extensao)

                    caract_escritos = b''
                    
                    #serve para concatecar todos os elementos de bytes
                    for char in leitura_arquivo:
                        caract_escritos += char
                    
                    if extensao == None:
                        extensao = "text/txt"
                        retorno = estabelece_plataforma
                        mensagem = (b'HTTP/1.1 200 OK'
                                    b'\r\nServer: Local Teste'
                                    b'\r\nSystem: ' + sistema.encode() + versao_sistema.encode() +
                                    b'\r\nDate: ' + data_e_horario.encode() + b' UTC'
                                    b'\r\n' + dados_do_cabecalho[2].encode() +
                                    b'\r\nAllow: ' + dados_do_cabecalho[0].split()[0].encode() +
                                    b'\r\nContent-Type: text/html; charset=utf-8\r\n\r\n')
                        
                        mensagem += (f'<!DOCTYPE html>'
                                    f'\r\n<html lang="pt-br">'
                                    f'\r\n<head>'
                                    f'\r\n<meta name = "viewport" content = "width=device-wwidth, initial-scale=1.0">'
                                    f'\r\n<title>Olá, essa e uma página de testes</title>'
                                    f'\r\n<link rel="icon" type="image/x-icon" href="favicon.ico">'
                                    f'\r\n<link rel="stylesheet" href="./styleProjRedes.css">'
                                    f'\r\n</head>'
                                    f'\r\n<body>'
                                    f'\r\n<nav>'
                                    f'\r\n<a href="ler{st+arquivo_requisitado}"><input type="submit" value="Ler arquivo codificado em .TXT" class = "leitura"></a>'
                                    f'\r\n<a href="{st+arquivo_requisitado}" download><input type="submit" value="Download" class = "download"></a>'
                                    f'\r\n<a href="{st+retorno}"><input type="submit" value="Retornar" class = "retornar"></a>'
                                    f'\r\n<nav>').encode()
                        
                        print(mensagem)
                    else:
                        bits = str(len(caract_escritos))

                        #cabecalho
                        mensagem = (b'HTTP/1.1 200 OK'
                                    b'\r\nServer: Local Teste'
                                    b'\r\nSystem: ' + sistema.encode() + versao_sistema.encode() +
                                    b'\r\nDate: ' + data_e_horario.encode() + b' UTC'
                                    b'\r\n' + dados_do_cabecalho[2].encode() +
                                    b'\r\nAllow: ' + dados_do_cabecalho[0].split()[0].encode() +
                                    b'\r\nContent-Length: ' + bits.encode() +
                                    b'\r\nContent-Type: ' + extensao.encode() + b'; charset=utf-8\r\n\r\n')
                        
                        mensagem += caract_escritos

                    socket_cliente.send(mensagem)
                    
                    print(diretorio_atual, '<--')
                    print('-'*50)
                    
                except:
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
                                 '\r\n<meta name="viewport" content="width=device-width, initial-scale=1.0">'
                                 '\r\n<meta charset = "utf-8">'
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