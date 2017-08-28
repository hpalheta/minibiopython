# coding: utf-8
'''
  
    Programa  : bio04_trans.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  bio04_trans.py

''' 
#importando Seq e IUPAC
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


#declarando varável seq_dna
seq_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)

#print sequencia
print ("Sequência DNA    :5' %s 3' \n" % (seq_dna))

#DNA template
template_dna = seq_dna.reverse_complement()

#print template
print ("Template DNA     :3' %s 5' \n" % (template_dna))

#RNA pelo template
rna_v2 = template_dna.reverse_complement().transcribe()
print ("RNA              :5' %s 3' \n" % (rna_v2))

#RNA pela seq DNA
rna_v1 = seq_dna.transcribe()
print ("RNA              :5' %s 3' \n" % (rna_v1))




