# coding: utf-8
'''
  
    Programa  : py03_operadores.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  py03_operadores.py

''' 
#tabela apoio
'''
=====  =========================  ==========================
Tipo     Descrição                Ex: 
=====  =========================  ==========================
(+)    Soma                       res = 3 + 1, x = a + b 
(-)    Subtração                  res = 9 - 1, x = a - b                          
(*)    Multiplicação              res = 2 * 3, x = a x b
(/)    Divisão.                   res = 10 / 2, x = a / b 
(%)    Módulo (resto)             res = 10 % 3, x = a % b
(**)   Potenciação                res = 2**2, x = a ** b
(//)   Divisão Resultado Inteiro  res = 10 // 3 , x = a // b
=====  =========================  ==========================
'''

#função print
print("Testando operadores")
print("\n");

#Variavel a recebe valor 10
a = 10

#Variável b recebe valor 3
#print
b = 3

#Variável x recebe soma a + b
x = a + b

#print da operação
print("Operacao (x = a + b) %d + %d = %d " %(a,b,x))
print("\n");

#Variável x recebe subtracao a - b
x = a - b
#print da operação
print("Operacao (x = a - b) %d - %d = %d " %(a,b,x))
print("\n");

#Variável x recebe multiplicacao a * b
x = a * b
#print da operação
print("Operacao (x = a * b) %d * %d = %d " %(a,b,x))
print("\n");


#Variável x recebe divisão a / b
x = a / b
#print da operação
print("Operacao (x = a * b) %d / %d = %f " %(a,b,x))
print("\n");


#Variável x recebe divisão inteiro a // b
x = a // b
#print da operação
print("Operacao (x = a // b) %d // %d = %d " %(a,b,x))
print("\n");


#Variável x recebe modulo a / b
x = a % b
#print da operação
print("Operacao (x = a %% b) %d %% %d = %d " %(a,b,x))
print("\n");


#Variável x recebe potencia a ^ b
x = a ** b
#print da operação
print("Operacao (x = a ** b) %d ** %d = %d " %(a,b,x))
print("\n");



