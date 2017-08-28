# coding: utf-8
'''
  
    Programa  : bio08_fastasave.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  bio08_fastasave.py

''' 
#importando Seq
from Bio import SeqIO

#variavel arquivo entrada e saida
arquivo_entrada = open("multi.fasta","r")
arquivo_saida   = open("multi_result.fasta","w")

print ("Executando leitura")    
#lendo o arquivo entrada
for i in SeqIO.parse(arquivo_entrada, "fasta"):    
	#caso a sequencia tenha tamanho maior >= 30 escreva no arquivo
	if (len(i.seq) >= 30):
		SeqIO.write(i, arquivo_saida, "fasta")

#Não esqueça de fechar o arquivo
arquivo_saida.close()
print ("Arquivo Salvo")    
