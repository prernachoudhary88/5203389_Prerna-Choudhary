def counterGame(n):
    moves = 0
    
    while n != 1:
       
        if (n & (n - 1)) == 0:
            n = n // 2
        else:
            highest_power = 1 << (n.bit_length() - 1)
            n = n - highest_power
        moves += 1
      
    if moves % 2 == 0:
        return "Richard"
    else:
        return "Louise"
