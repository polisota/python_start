def SumRec(a, b):    
    a -= 1
    b += 1
    if a > 0:
        return SumRec(a, b)
    return b

def MulRec(a, b):       
    if b == 0:
        return 1
    return a * MulRec(a, b - 1)