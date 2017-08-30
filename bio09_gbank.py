# coding: utf-8
'''
  
    Programa  : bio09_gbank.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  bio09_gbank.py

''' 
#importando Seq
from Bio import SeqIO

#variavel gbkparse.
genbak_parse = SeqIO.parse("NC_009926.gbk", "genbank")

for seq_record in  genbak_parse:

    # imprime o cabecalho
    print(seq_record.id)

    # imprime a sequencia
    print(seq_record.seq[0:100])

    # imprime o tamanho da sequencia
    print(len(seq_record))

