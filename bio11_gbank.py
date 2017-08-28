# coding: utf-8
'''
  
    Programa  : bio11_gbank.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  bio11_gbank.py

''' 
#importando Seq
from Bio import SeqIO

#variavel gbk
genbak_seq = SeqIO.read("NC_009926.gbk", "genbank") 

#print informações do obejto genbank
print(genbak_seq)

#print extraindo somente o fasta 300 bases.
print(genbak_seq.format("fasta")[0:300])	

#salvando arquivo fasta
SeqIO.convert("NC_009926.gbk", "genbank", "NC_009926.fasta", "fasta")	