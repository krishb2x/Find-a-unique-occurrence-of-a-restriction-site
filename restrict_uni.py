def restrict_uni(dna, enz):
    """ find unique restriction sites """
    
    found = None
    site = dna.find(enz)
    
    while site != -1:
        if found:
            break
        found = site
        site = dna.find(enz, found+1)
    else:
        if found is not None:
            return found
