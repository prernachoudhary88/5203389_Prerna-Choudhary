class TrieNode:
    def __init__(self):
        self.c = {}
        self.e = False

def noPrefix(words):
    r = TrieNode()

    for word in words:
        node = r
        for i, char in enumerate(word):
            if char not in node.c:
                node.c[char] = TrieNode()
            node = node.c[char]

            if node.e:
                print("BAD SET")
                print(word)
                return
        
        if node.c:
            print("BAD SET")
            print(word)
            return
        node.e = True

    print("GOOD SET")
