def reverse(llist):
    curr = llist
    head = None

    while curr:
        curr.prev, curr.next = curr.next, curr.prev
        
        head = curr

        curr = curr.prev

    return head
