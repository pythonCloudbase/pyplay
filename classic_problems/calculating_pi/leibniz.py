# leibniz formula 
#  4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11

def calculate_pi(no_of_terms):
    numerator = 4.0
    denominator = 1.0
    term_sum = 0.0
    operator = 1.0
    for _ in range(no_of_terms):
    
        term_sum += operator * numerator/denominator
        denominator += 2
        operator *= -1

    return term_sum


if __name__ == "__main__":
    print(calculate_pi(10000000))

