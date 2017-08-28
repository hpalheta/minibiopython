# coding: utf-8
'''
  
    Programa  : bio05_tradu.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  bio05_tradu.py

''' 
#importando Seq e IUPAC
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


#declarando varável seq_dna
seq_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)

#print sequencia
print ("Sequência DNA         : %s  \n" % (seq_dna))

#RNA pela seq DNA
rna = seq_dna.transcribe()
print ("RNA                   : %s  \n" % (rna))

#declarando varável tradução
traducao_v1 = rna.translate();

#print traducao
print ("Tradução *  do RNA    : %s \n" % (traducao_v1))

#declarando varável tradução
traducao_v2 = seq_dna.translate()

#print traducao
print ("Tradução * direto DNA : %s \n" % (traducao_v2))

#declarando varável traducao
traducao_v3 = seq_dna.translate(to_stop=True)

#print traducao com stop
print ("Tradução  DNA (Stop)  : %s \n" % (traducao_v3))


#declarando varável traducao
traducao_v3 = seq_dna.translate(table=2)

#print traducao mitocondrial
print ("Tradução Tabela2 DNA  : %s \n" % (traducao_v3))

#print traducao mitocondrial com stop
traducao_v3 = seq_dna.translate(table=2, to_stop=True)

#print traducao
print ("Tradução DNA T2(Stop) : %s \n" % (traducao_v3))





