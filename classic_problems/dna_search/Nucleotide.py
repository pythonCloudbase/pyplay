from enum import IntEnum
from typing import Tuple, List

Nucleotide = IntEnum('Nucleotide', ('A','C','G','T'))

# we are using IntEnum so that we can use >,<,=
# A tuple pf 3 nucleotides is kknown as codons

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


# they dont really care about us
# torn
# biiter sweet symphony
# livin la vida loca
# everybody
# earth song
# children
# rythm of the night
# genie in abottle
# scatman
# all star smash mouth
#california love
# somewhere over the rainbow
# blue de daa bu dee
# macarena
# zombies
# smells like tten spirit

def string_to_gene(s):
    gene = []
    for i in range(0, len(s), 3):
        if (i+2) >= len(s):
            return gene
        codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    
    return gene

my_gene = string_to_gene(gene_str)

print(my_gene)