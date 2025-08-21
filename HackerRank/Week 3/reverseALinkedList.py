def reverse(llist):
    prev = None
    curr = llist

    while curr:
        next_node = curr.next  
        curr.next = prev      
        prev = curr          
        curr = next_node       

    return prev 
