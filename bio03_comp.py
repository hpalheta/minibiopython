# coding: utf-8
'''
  
    Programa  : bio03_comp.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  bio03_comp.py

''' 
#importando Seq 
from Bio.Seq import Seq

#declarando varável sequencia
sequencia = Seq('CATGTGCTATGGTT')


#print sequencia
print ("Sequência    :5' %s 3' têm %i bases\n" % (sequencia,len(sequencia)))


#print complementar 
print ("Complementar :3' %s 5' \n" % (sequencia.complement()))

#print reverso 
print ("Reverso      :5' %s 3' \n" % (sequencia.reverse_complement()))


