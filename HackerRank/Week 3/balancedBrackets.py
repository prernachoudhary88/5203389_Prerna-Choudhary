def isBalanced(s):
    stack = []
    b = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in b.values():  
            stack.append(char)
        elif char in b:  
            if not stack or stack[-1] != b[char]:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"
