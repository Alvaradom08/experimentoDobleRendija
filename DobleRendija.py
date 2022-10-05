import matplotlib.pyplot as plot
import numpy as np

from calculadora import *

def mtrxFinal (mtrx):
    j, i = len(mtrx), len(mtrx)
    for i in range(i):
        newI= []
        for j in range(j):
            newI.append([(modulo(mtrx[i][j]) ** 2), 0])
            mtrx[i] = newI
    return mtrx

def probaQuantSys (mtrx, vecI, clicks):
    res = -1
    if clicks >= 0 and type(clicks) is int:
        long = len(vecI)
        cpMtrx = mtrx[:]

        for x in range(clicks):
            mtrx = multimatriz(mtrx,cpMtrx)
        res = mtrxFinal(mtrx)
    return res
def experimentoMultiple (mtrx, vecI, clicks):
    return probaQuantSys(mtrx, vecI, clicks)

def graficoProbabilidad (vec):
    inf = len(vec)
    x = np.array([x for x in range(inf)])
    y = np.array([round(vec[x][0]*100,2) for x in range(inf)])

    plot.bar(x, y, color='r', aling='center')
    plot.title('Probalbilidades Vector')
    plot.show()