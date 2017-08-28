# coding: utf-8
'''
  
    Programa  : py11_funcao.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  py11_funcao.py

''' 

#Definindo funcão imprimir_nome na qual e passado nome
def imprimir_nome(nome):
	print("Olá , %s!" %nome)


#Definindo funcão que junta dois nomes e possui retorno
def junta_nome(nome,sobrenome):
    return nome + " "+ sobrenome


#fazendo uso da função 
imprimir_nome("Ana")

#fazendo uso da função imprimir_nome passando o 
#retorno da chamada da funcao junta_nome
imprimir_nome(junta_nome("Ana","Maria"))
