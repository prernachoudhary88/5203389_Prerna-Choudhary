from collections import Counter

def isValid(s):
    freq = Counter(s)
    freq_values = list(freq.values())
    
    freq_count = Counter(freq_values)
    
    if len(freq_count) == 1:
        
        return "YES"
    
    if len(freq_count) == 2:
        key1, key2 = freq_count.keys()
        val1, val2 = freq_count[key1], freq_count[key2]
        
        if (val1 == 1 and (key1 - 1 == key2 or key1 == 1)) or \
           (val2 == 1 and (key2 - 1 == key1 or key2 == 1)):
            return "YES"
    
    return "NO"
