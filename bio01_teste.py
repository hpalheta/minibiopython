# coding: utf-8
'''
  
    Programa  : bio01_teste.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  bio01_teste.py

''' 
#importando Seq 
import Bio

from Bio.Seq import Seq

#ver
print(Bio.__version__)

#declarando varável sequencia
sequencia = Seq('CATG')

#print sequencia
print ("Sequência %s têm %i bases" % (sequencia,len(sequencia)))








