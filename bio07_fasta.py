# coding: utf-8
'''
  
    Programa  : bio07_fasta.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  bio07_fasta.py

''' 
#importando Seq
from Bio import SeqIO

#variavel arquivo entrada
arquivo_entrada = "NC_005816.fasta"

#variavel com objeto de leitura de arquivo fasta
record = SeqIO.read( arquivo_entrada, "fasta")

#print
print("Detalhe do Arquivo fasta :"+ arquivo_entrada)
print(record)
print("\n")

#de uma outra maneira
for i in SeqIO.parse(arquivo_entrada, "fasta"):

    # imprime o cabecalho
    print ("ID: %s  \n" % (i.id))    

    print ("Name: %s  \n" % (i.name))

    print ("Description: %s  \n" % (i.description))
 
    # imprime a sequencia 30 bases
    print ("Seq: %s...  \n" % (i.seq[0:30]))
    

    # imprime o tamanho da sequencia
    print ("Length: %s  \n" % (len(i)))
    
