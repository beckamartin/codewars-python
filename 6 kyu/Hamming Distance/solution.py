def hamming(a,b):
    resault = 0

    for pos, char in enumerate(a):
        if char not in b[pos]:
            resault += 1

    return resault