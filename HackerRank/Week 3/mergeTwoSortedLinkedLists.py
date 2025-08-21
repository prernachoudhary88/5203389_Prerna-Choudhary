def mergeLists(h1, h2):
    
    d = SinglyLinkedListNode(0)
    t = d

    while h1 and h2:
        if h1.data <= h2.data:
            t.next = h1
            h1 = h1.next
        else:
            t.next = h2
            h2 = h2.next
        t = t.next

    if h1:
        t.next = h1
    elif h2:
        t.next = h2

    return d.next
