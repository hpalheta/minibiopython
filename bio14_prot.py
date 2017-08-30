# coding: utf-8
'''
  
    Programa  : bio14_prot.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com> 

    Execução:
      python  bio14_prot.py

''' 
#importando  

from Bio import ExPASy, SwissProt


#fazendo busca pelo Id
# 'O23729', 'O23730', 'O23731', Chalcone synthases from Orchid
# http://www.uniprot.org/uniprot/O23729

ids = ['O23729', 'O23730', 'O23731']

for id in ids:
    handle = ExPASy.get_sprot_raw(id)
    record = SwissProt.read(handle)
    print("Descricao: %s" % record.description)
    for ref in record.references:
        print("Autores: %s" % ref.authors)
        print("Titulo: %s" % ref.title)

    print("Classificação: %s" % record.organism_classification)
    print("")

		