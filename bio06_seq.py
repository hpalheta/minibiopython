# coding: utf-8
'''
  
    Programa  : bio06_seq.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  bio06_seq.py

''' 
#importando Seq e IUPAC
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#declarando varável seq
seq_dna_parte1 = Seq("GATCGATGGG", IUPAC.unambiguous_dna)

seq_dna_parte2 = Seq("CCTATATAGGA", IUPAC.unambiguous_dna)

seq_dna_parte3 = Seq("TCGAAAATCGC", IUPAC.unambiguous_dna)

#concatenando sequencias
seq_dna = seq_dna_parte1 + seq_dna_parte2 + seq_dna_parte3



#print sequencia
print ("Sequência DNA             : %s  \n" % (seq_dna))

#print em parte da sequencia da posicao 4 a 12
print ("Sequência 4 a 12          : %s  \n" % (seq_dna[4:12]))

#print as primeira letras de 3 em 3 letras
print ("Sequência letra de 3 em 3 : %s  \n" % (seq_dna[::3]))

#print em parte da sequencia da posicao 4 a 12
print ("Sequência reversa         : %s  \n" % (seq_dna[::-1]))


