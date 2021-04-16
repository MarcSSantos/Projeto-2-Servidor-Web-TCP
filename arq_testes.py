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