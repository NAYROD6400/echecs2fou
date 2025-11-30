def creerEchiquier():
    echiquier = []
    for _ in range(8):
        echiquier.append([])
        for i in range(8):
            echiquier[_].append(' ')
    return echiquier

def afficherEchiquier(echiquier):
    for i in range(8):
        print(echiquier[i])

echiquier = creerEchiquier()
afficherEchiquier(echiquier)
