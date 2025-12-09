

def creerEchiquier():
    echiquier = []
    for _ in range(8):
        echiquier.append([])
        for i in range(8):
            echiquier[_].append(' ')
    return echiquier


def afficherEchiquier(echiquier):
    for ligne in range(8):
        print("")
        for i in range(8):
            print(echiquier[ligne][i], end=' ')


def placerPiece(echiquier):
    # Placement des pions (p)
    for pion in range(8):
        echiquier[1][pion] = 'P'
        echiquier[6][pion] = 'p'

    # Placement des Tours (t) Cavaliers (c) Fous (f) Roi (r) et Dale (d)
    echiquier[0][0], echiquier[0][7] = 'T', 'T'
    echiquier[7][0], echiquier[7][7] = 't', 't'
    echiquier[0][1], echiquier[0][6] = 'C', 'C'
    echiquier[7][1], echiquier[7][6] = 'c', 'c'
    echiquier[0][2], echiquier[0][5] = 'F', 'F'
    echiquier[7][2], echiquier[7][5] = 'f', 'f'
    echiquier[0][3], echiquier[0][4] = 'D', 'R'
    echiquier[7][3], echiquier[7][4] = 'd', 'r'

    return echiquier


plateau = creerEchiquier()
afficherEchiquier(placerPiece(plateau))
