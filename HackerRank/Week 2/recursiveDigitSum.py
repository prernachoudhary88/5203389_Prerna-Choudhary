def superDigit(n, k):
    
    def get_super_digit(x):
        if len(x) == 1:
            return int(x)
        else:
            s = sum(int(d) for d in x)
            return get_super_digit(str(s))

    initial_sum = sum(int(d) for d in n) * k
    return get_super_digit(str(initial_sum))
