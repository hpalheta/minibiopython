# coding: utf-8
'''
  
    Programa  : bio16_filo.py
    Homepage  : http://www
    Autor     : Biopython

    Execução:
      python  bio16_filo.py

''' 
#importando  

from Bio import Phylo
tree = Phylo.read("simple.dnd", "newick")
print(tree)


Phylo.draw_ascii(tree)

tree.rooted = True

Phylo.draw(tree)

tree = tree.as_phyloxml()

from Bio.Phylo.PhyloXML import Phylogeny

tree = Phylogeny.from_tree(tree)

tree.root.color = (128, 128, 128)

mrca = tree.common_ancestor({"name": "E"}, {"name": "F"})

mrca.color = "salmon"

tree.clade[0, 1].color = "blue"

Phylo.draw(tree)