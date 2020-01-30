string1 = input('Enter sequence 1 : ')
string2 = input('Enter sequence 2 : ')

m = len(string1)
n = len(string2)

# returns all subsequences as an array
def get_all_subsequences(string1,m):
    string_array = []
    for i in range(m):
        for k in range(m-i):
            sub_str = ""
            for j in range(i+1):
                if(k+j < m):
                    sub_str += string1[k+j]
            string_array.append(sub_str)

    return string_array 

sequences1 = get_all_subsequences(string1, m)
sequences2 = get_all_subsequences(string2, n)

# print(sequences1)
# print(sequences2)


def find_max_subsequence(sequences1, sequences2):
    found = False
    max_value  = ""
    for i in sequences1:
        for j in sequences2:
            if(i == j and len(i) > len(max_value)):
                found = True
                max_value = i
    
    if found == True:
        print("Max subseqence that occurs in both is ", max_value)
    else:
        print("Completely different subsequences !")


find_max_subsequence(sequences1, sequences2)