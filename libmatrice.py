def det2(mat):
    '''
    Calcul le déterminant d'une matrice 2x2
    '''
    return mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1]


def det3(mat):
    '''
    Calcul le déterminant d'une matrice 3x3
    '''
    return


def reduit(mat, ligne, colonne):
    '''
    Calcul d'une matière réduite
    '''
    res=[[0,0],[0,0]]
    ml=0
    for l in range(3):
        mc=0
	if l != ligne:
            for c in range(3):
                if c != colonne:
                    res[ml][mc] = mat[l][c]
                    mc += 1
                ml += 1
    return res
