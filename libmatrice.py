def det2(mat):
    '''
    Calcul d'un déterminan d'une matrice 2x2
    '''
    return mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1]

def det3(mat):
    '''
    Calcul d'un déterminant 3x3
    '''
    return mat[0][0]*(mat[1][1]*mat[2][2]-mat[2][1]*mat[1][2]) - mat[1][0]*(mat[0][1]*mat[2][2]-mat[2][1]-mat[0][2]) + mat[0][2]*(mat[0][1]*mat[1][2]-mat[1][1]*mat[0][2])

def reduit(mat, ligne, colonne):
    '''
    Calcul d'une matrice réduite
    '''
    res = [[0, 0], [0, 0]]
    ml = 0
    for l in range(3):
        mc = 0
        if l != ligne:
            for c in range(3):
                if c != colonne:
                    res[ml][mc] = mat[1][c]
                    mc += 1
                ml += 1
    return res
