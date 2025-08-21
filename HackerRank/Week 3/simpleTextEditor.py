def simpleTextEditor(operations):
    s = []
    h = []
    result = []
    
    for op in operations:
        parts = op.split()
        cmd = parts[0]

        if cmd == '1':  
            h.append(''.join(s))  
            s.extend(parts[1])
        
        elif cmd == '2': 
            h.append(''.join(s))  
            k = int(parts[1])
            s = s[:-k]
        
        elif cmd == '3':  
            k = int(parts[1])
            result.append(s[k-1])
        
        elif cmd == '4': 
            s = list(h.pop())
    
    return result
    
if __name__ == '__main__':
    q = int(input()) 
    operations = [input().strip() for _ in range(q)]

    output = simpleTextEditor(operations)

    for line in output:
        print(line)
