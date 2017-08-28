# coding: utf-8
'''
  
    Programa  : bio12_blast.py
    Homepage  : http://www
    Autor     : Helber Palheta  <hpalheta@outlook.com>

    Execução:
      python  bio12_blast.py

''' 
#importando  NCBI e Seq 
from Bio.Blast import NCBIWWW 
from Bio import SeqIO

#variavel fasta padrao
fasta_padrao = SeqIO.read("blast.fasta", format="fasta")

#criando variavel como o arquivo de busca fasta
print("-------------------------------------------------------------------------------")
print("-Busca no Blast")
print("-------------------------------------------------------------------------------")
print("Fasta Padrao:")
print(fasta_padrao.format("fasta")[0:130]+"...")
print("-------------------------------------------------------------------------------")


entrada_fasta = input("-Informe caminho do aruivo fasta ou vazio para padrão: ")

if entrada_fasta !="":
   print("Arquivo informado:"+entrada_fasta)
   arquivo_busca = SeqIO.read(entrada_fasta, format="fasta")
else:
  print("Arquivo Padão selecionado")
  arquivo_busca = fasta_padrao

print("-------------------------------------------------------------------------------")

print("Iniciando procura no NCBI")

#Executado busca no blast e pedindo retorno Txt
resposta = NCBIWWW.qblast("blastn", "nt", arquivo_busca.seq, format_type="Text")

print("-------------------------------------------------------------------------------")
print(resposta.read())
print("-------------------------------------------------------------------------------")
print("Fim.")
