def det2(arg):
    return (arg[0][0] * arg[1][1] - arg[0][1] * arg[1][0])


def reduit(mat, ligne, colonne):
    res = [[0,0],[0,0]]
    ml = 0
    for l in range(3):
        mc = 0
        if l != ligne:
            for c in range(3):
                if c != colonne:
                    res[ml][mc] = mat[l][c]
                    mc += 1
            ml +=1
    return res


def det3(arg):
    return arg[0][0] * det2(reduit(arg,0,0)) - arg[0][1] * det2(reduit(arg,0,1)) + arg[0][2] * det2(reduit(arg,0,2))
