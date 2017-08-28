# coding: utf-8
'''
  
    Programa  : py04_if.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  py04_if.py

''' 
#variável base de nucleotido
base = input("Informe a primeira base da sequencia de nucleotidios: ")

#função print
print("Base N. Informada: "+base);

if ((base == "A") or (base == "a")):
   print(" É uma Adenina")
elif ((base == "T") or (base == "t")): 
	print(" É uma Tinina")
elif ((base == "G") or (base == "g")):  
	print(" É uma Guanina")
elif ((base == "C") or (base == "c")): 
	print(" É uma Citosina")		
else:
	print(" Não determinado")	

