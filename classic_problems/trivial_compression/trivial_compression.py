class CompressedGene:
    def __init__(self, gene):
        self.compress(gene)
    
    def compress(self, gene):
        self.bit_string = 1

        for nucleotide in gene.upper():
            self.bit_string <<=2
            if nucleotide == "A":
                self.bit_string |= 0b00
            
            elif nucleotide == "C":
                self.bit_string |= 0b01
            
            elif nucleotide == "G":
                self.bit_string |= 0b10
            
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".form)

    def decompress(self):
        gene = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueEror("Invalid bits:{}".format(bits))

        return gene[::-1]
    
    def __str__(self):
        return self.decompress()

    
if __name__ == "__main__":
    from sys import getsizeof
    stringg = "TATATATGCTTATGCTACGCTACTAGCGATCGATCAGCTAGCTAGCTGATAGTCAGCATGCATCGCTAGTG" * 100
    # print("original string: ")
    # print(stringg)
    print("original size: ",getsizeof(stringg))
    compressedGene = CompressedGene(stringg)
    # print("decompressed: ")
    # print(compressedGene)
    print("compressed size: ", getsizeof(compressedGene))
    