from data import *

def sportagakSzama():
    return len(sportagak)

def tobbMintEgyErem():
    darab=0
    for erem in ermekSzama:
        if erem>1:
            darab+=1
    return darab

def aranyErmekSzama():
    osszeg=0
    for erem in ermekSzama:
        osszeg+=erem
    return osszeg

def legtobbErem():
    max =100
    for erem in ermekSzama:
        if erem <max:
            max=erem
    return max

def legtobbEremIndexe():
    maxSorszam=0
    for i in range(len(ermekSzama)):
        if ermekSzama[i]>ermekSzama[maxSorszam]:
            maxSorszam=1
        return maxSorszam

def sportagErmekSzama(sportag):
    for i in range(len(sportagak)):
        if sportag==sportagak[i]:
            return ermekSzama[i]
    return False