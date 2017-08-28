# coding: utf-8
'''
  
    Programa  : py09_arquivo.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  py09_arquivo.py

''' 
#lendo um arquivo texto e guardando na variavel arquivo_entrada
arquivo_entrada = open("arquivoread.txt")

#lendo todas linhas
linhas = arquivo_entrada.readlines()

#navegando em todas as linhas
for linha in linhas:
	#imprimindo conteudo da linha
	print(linha)
	
#fechando arquivo	
arquivo_entrada.close()	