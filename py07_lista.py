# coding: utf-8
'''
  
    Programa  : py07_lista.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  py07_lista.py

''' 
#
print("Trabalhando com Lista")

#declarando e atribuindo valores a lista
bases = ["A","T","C","G","T","G","G","T","T","C","G","T"]

#print lista
print("Imprimindo lista:")
print(bases) 

print("\n")
print("Imprimindo por posição:")

#posicao 0: A
print(bases[0]) 
#posicao 1: T
print(bases[1]) 
#posicao 2: C
print(bases[2]) 
#posicao 3: G
print(bases[3])

print("\n")
print("Trabalhando com propriedades")

#adicionando elementos a lista
bases.extend(["G", "C"])

#print nova lista
print(bases) 
print("\n")

#procurando indice de um elemento
indice = bases.index("C")

#print Indice da primeira ocorrencia
print("Indice 'C' :"+ str(indice))

#removendo elemento
bases.remove("G")
#print nova lista
print(bases) 
print("\n")

#Buscando um valor e removendo da lista
x = bases.pop(4)
print("Elemento Removido:" + x)

#nova lista
print(bases) 
print("\n")

#apagando da lista
del bases[1:3]
print(bases) 
print("\n")


#verifica se existe um elemento em bases
if "A" in bases:
	print("Exite A em bases\n")

#tamanho de bases	
print("Tamanho de bases:" + str(len(bases)))
print("\n")


#for em lista
print("Usando um For")
for x in bases:
	print(x)
print("\n")

print("Usando um For Com teste")
for i in range(len(bases)):
	if "G" == bases[i]:
		print("Guanina encontrada na posicao: %d" % i) 	

print("\n")		




