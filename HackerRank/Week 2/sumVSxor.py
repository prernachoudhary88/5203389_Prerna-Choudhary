def sumXor(n):
    
    if n == 0:
        return 1
    
    count_zero_bits = 0
    for bit in bin(n)[2:]:
        if bit == '0':
            count_zero_bits += 1
    
    return 2 ** count_zero_bits
