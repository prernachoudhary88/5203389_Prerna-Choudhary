def insertNodeAtPosition(llist, data, pos):
    new = SinglyLinkedListNode(data)
    
    if pos == 0:
        new.next = llist
        return new

    curr = llist
    index = 0

    while index < pos - 1:
        curr = curr.next
        index += 1

    new.next = curr.next
    curr.next = new

    return llist
