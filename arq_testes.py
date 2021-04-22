a = 'a b c d e'
b = a.split()[0:3]
print(b)

def join_method(lista):
  return ''.join(['\\'+x if x != lista[0] else x for x in lista])

b = join_method(a.split()[0:3])
print(b)

d = 'C:\Projeto_servidor_web\\arq\omega'
g = d.replace('arq\omega', '')
print(g)

import os
import time

pasta_ou_arquivo = os.path.isfile('C:\Projeto_servidor_web\\arq_testes.py')
print(pasta_ou_arquivo)

modificacao = os.path.getmtime(g)
modificacao_local = time.ctime(modificacao)
print(modificacao_local)

i = [1,2,3,4]
i.pop(len(i)-1)
print(i)

def kk():
  lista = [0,1,2,3,4]
  return lista

j = kk()[0:2]
print(j, 'bumbum')


u = ['']
print(u[-1],'aaaa')

def pop_dir(diretorio):
    # C:\Projeto_servidor_web\arq\omega
    restringir = diretorio.split('\\')
    if restringir[-1] != 'arq':
        restringir.pop(len(restringir)-1)
        
        if restringir[-1] == 'arq':
            return ['']
        else:
            return restringir
    
    else:
        return  ['']
      
sim = ''      
ll = f'{"g"}'
print(ll)

#                if arquivo_requisitado == '\\abacate':
#                    lista_back_dir = pop_dir(diretorio_atual)
#                    diretorio_atual = join_method(lista_back_dir)

for x in range(0, 0):
  print('pipoca')
  
t  = [8,7,6,4]

yy = t.index(8)
print(yy) 

def join_method(lista):
  return ''.join(['\\'+x if x != lista[0] else x for x in lista])


ii = ['a','b','c','d']
uu = join_method(ii)
print(uu)

for x in range(2,3):
  print(x)
