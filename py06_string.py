# coding: utf-8
'''
  
    Programa  : py06_string.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  py06_string.py

''' 

#função print
print("Trabalhando com String")


#Variavel a recebe valor 10
a = 10

#Variável b recebe valor 3
b = 3

#Variável x recebe soma a + b
x = a + b

#print da operação
print("Operacao (x = a + b) %d + %d = %d " %(a,b,x))
print("\n");

#convertendo em string 
print("Operacao (x = a + b) "+str(a)+" + "+str(b)+" = "+str(x))
print("\n");

#declarando variavel curso
str_curso = "Biopython"

print("-Curso:"+str_curso+"\n")

print("-Tamanho da String:"+ str(len(str_curso)) +"\n")

print("-SubString: 0-3 "+ str_curso[0:3] +"\n")

print("-SubString: 7 "+ str_curso[6] +"\n")




