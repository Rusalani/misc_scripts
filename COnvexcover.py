
import math
import random
import numpy as np
#from matplotlib import pyplot as plt

def find_convex_cover(pvertices,clist):
    '''

    :param n:
    :param m:
    :param niter:
    :return:
    '''

    fig,ax = plt.subplots()
    x=[]
    y=[]
    for i in pvertices:
        x.append(i[0])
        y.append(i[1])
    x.append(x[0])
    y.append(y[0])
    ax.plot(x,y)
    #plt.plot(clist)
    #plt.show()
    x = []
    y = []
    for i in clist:
        x.append(i[0])
        y.append(i[1])
    plt.scatter(x,y)
    plt.show()
    for i in pvertices:
        d=[]
        for y in clist:
            d.append(abs(y-i))
    return None










pvertices = [[ 0.573,  0.797],
                        [ 0.688,  0.402],
                        [ 0.747,  0.238],
                        [ 0.802,  0.426],
                        [ 0.757,  0.796],
                        [ 0.589,  0.811]]

clist = [(0.7490863467660889, 0.4917635308023209),
              (0.6814339441396109, 0.6199470305156477),
              (0.7241617773773865, 0.6982813914515696),
              (0.6600700275207232, 0.7516911829987891),
              (0.6315848053622062, 0.7730550996176769),
              (0.7348437356868305, 0.41342916986639894),
              (0.7597683050755328, 0.31729154508140384)]
print(find_convex_cover(pvertices,clist))

