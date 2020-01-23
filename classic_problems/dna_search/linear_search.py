import Nucleotide as n

def linear_search(mygene, targetCodon):
    for codon in mygene:
        if codon == targetCodon:
            return True
        else :
            return False

acg = (n.Nucleotide['A'], n.Nucleotide['C'], n.Nucleotide['G'])

if(linear_search(n.my_gene, acg)):
    print("found !")
else:
    print("look elsewhere !")