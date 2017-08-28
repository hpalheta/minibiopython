# coding: utf-8
'''
  
    Programa  : py10_arquivo.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  py10_arquivo.py

''' 

print("Escrevendo arquivo.")

#lendo um arquivo texto e guardando na variavel arquivo_entrada
arquivo_saida = open("arquivowrite.txt","w+")

#lista de linhas para o arquivo
linhas_lista = ["BioPython 01","BioPython 02","BioPython 03","BioPython 4","BioPython 5"]


#navegando na lista e escrevendo no arquivo
for linha in linhas_lista:
    arquivo_saida.write(linha)
    arquivo_saida.write("\n")

#fechando o arquivo 
arquivo_saida.close()    

print("Arquivo Criado.")