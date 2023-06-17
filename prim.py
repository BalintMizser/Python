def prim(szam):
    if szam == 1:
        return False
    for i in range(2, szam):
        if szam % i == 0:
            return False
    return True
