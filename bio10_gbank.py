# coding: utf-8
'''
  
    Programa  : bio10_gbank.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  bio10_gbank.py

''' 
#importando Seq
from Bio import SeqIO

#variavel gbk
genbak_seq = SeqIO.read("NC_009926.gbk", "genbank") 


for i in genbak_seq.features:
	if i.type == 'CDS':
		print(i.qualifiers['product'])	
		#print(i.qualifiers['translation'])	
		