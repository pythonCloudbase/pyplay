class CompressedGene:
    def __init__(self, gene):
        self.compress(gene)
    
    def compress(self, gene):

        self.bit_string <<=2
        if nucleotide == "A":
            self.bit_string |= 0b00
        
        elif nucleotide == "C":
            self.bit_String |= 0b01
        
        elif nucleotide == "G":
            self.bit_string |= 0b10
        
        elif nucleotide == "T":
            self.bit_string |= 0b11
        else:
            raise ValueError("Invalid Nucleotide:{}".form)
