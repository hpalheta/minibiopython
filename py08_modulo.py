# coding: utf-8
'''
  
    Programa  : py08_modulo.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  py08_modulo.py

''' 
#importar todo um modulo
import os

#print path lib do python
print(os.path)


#importando elemento especifico
from  os import path
#print path lib do python direto
print(path)


#importando tudo de um modulo especifico
from  os import *

#print path lib do python direto
print(path)
