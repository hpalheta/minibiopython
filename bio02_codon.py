# coding: utf-8
'''
  
    Programa  : bio02_codon.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  bio02_codon.py

''' 
#importando CodonTable 
from Bio.Data import CodonTable

#declarando varável tabela_padrao
tabela_padrao = CodonTable.unambiguous_dna_by_id[1]

#declarando varável tabela_mito
tabela_mito   = CodonTable.unambiguous_dna_by_id[2]

#print na tabela basica
print(tabela_padrao)

#print na tabela mitocondrial
print(tabela_mito)



