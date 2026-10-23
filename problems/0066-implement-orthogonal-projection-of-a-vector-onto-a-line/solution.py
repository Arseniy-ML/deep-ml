def orthogonal_projection(v, L):
    """
    Compute the orthogonal projection of vector v onto line L.
    """
    element_1 = sum(x * y for x, y in zip(v, L))
    
    element_2 = sum(x * x for x in L)
    
    c = element_1 / element_2
    
    return [round(c * x, 3) for x in L]
