# coding: utf-8
'''
  
    Programa  : bio13_blast.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com> 

    Execução:
      python  bio13_blast.py

''' 
#importando  NCBI e Seq 
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


#variavel fasta padrao
fasta_busca = SeqIO.read("blast.fasta", format="fasta")

#criando variavel como o arquivo de busca fasta
print("-------------------------------------------------------------------------------")
print("-Busca no Blast e Salvando em XML")
print("-------------------------------------------------------------------------------")
print("Fasta Padrao:")
print(fasta_busca.format("fasta")[0:130]+"...")
print("-------------------------------------------------------------------------------")

print("Iniciando procura no NCBI ... Aguarde...")

#Executado busca no blast e pedindo retorno XML
resposta = NCBIWWW.qblast("blastn", "nt", fasta_busca.seq, format_type="XML")

print("-------------------------------------------------------------------------------")
print("Analisando e criando XML")
print("-------------------------------------------------------------------------------")

#arquivo de saida
xml_saida = open("saida_blast.xml", "w")

#escrevendo no arquivo
xml_saida.write(resposta.read())

#Sempre fechar o arquivo
xml_saida.close() 


# Fazendo a leitura do arquvio  XML, blast_resultado.xml

arquivo_xml = open("saida_blast.xml","r")
dados = NCBIXML.parse(arquivo_xml)
item = next(dados)

i = 1

for a in item.alignments:
	for hsp in a.hsps:
		print("Alinhamento.: %s  \n" % (i))
		print("Tamanho.....: %s  \n" % (a.length))
		print("Score.......: %s  \n" % (hsp.score))
		print("Gaps........: %s  \n" % (hsp.gaps))
		print("Query.......: %s  \n" % (hsp.query))
		print("match.......: %s  \n" % (hsp.match))
		print("sbjct.......: %s  \n" % (hsp.sbjct))
		i+=1

#fechando arquivo leitura
arquivo_xml.close()

print("Fim.")

		