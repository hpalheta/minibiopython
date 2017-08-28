# coding: utf-8
'''
  
    Programa  : py05_loop.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  py05_loop.py

''' 

#usando o for
print("Comando for:");
for i in range(10):
	if i == 5: 
		continue
	if i < 8:
		print(i)
	if i == 8:
		break


print("Comando while:");
i = 0
while i<=10:	
	if (i < 8) and (i != 5):
		print(i)
	
	if i == 8:
		break		
	i = i + 1



