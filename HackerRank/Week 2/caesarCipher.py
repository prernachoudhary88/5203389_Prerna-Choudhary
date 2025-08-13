def caesarCipher(s, k):
    result = []
    k = k % 26  

    for char in s:
        if char.isupper():
            shifted = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result.append(shifted)
        elif char.islower():
            shifted = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result.append(shifted)
        else:
            result.append(char)

    return ''.join(result)

if __name__ == '__main__':
    n = int(input())      
    s = input().strip()   
    k = int(input())      

    encrypted = caesarCipher(s, k)
    print(encrypted)
