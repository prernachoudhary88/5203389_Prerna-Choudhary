
def decodeHuff(root, s):
    curr = root
    for b in s:
        if b == '0':
            curr = curr.left
        else:
            curr = curr.right

        if curr.left is None and curr.right is None:
            print(curr.data, end='')
            curr = root  

