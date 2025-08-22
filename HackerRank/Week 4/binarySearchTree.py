def lca(r, v1, v2):
    
    if v1 > v2:
        v1, v2 = v2, v1

    while r:
        if r.info < v1:
            r = r.right
        elif r.info > v2:
            r = r.left
        else:
            return r
