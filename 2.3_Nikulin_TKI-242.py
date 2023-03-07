import math
import matplotlib.pyplot as plt
import numpy as np

Z = (1, -1.5)


def Module(z = Z):
    return (math.sqrt(math.pow(Z[0], 2) + math.pow(Z[1], 2)))

def ConjugateComplex(z = Z):
    return (z[0], -z[1])

def DivisionComplex(z1, z2):
    if (z2[0] != 0) and (z2[0] != 0):
        return ((z1[0]*z2[0] + z1[1]*z2[1])/(z2[0]**2 + z2[1]**2), (z1[1]*z2[0] - z1[0]*z2[1])/(z2[0]**2 + z2[1]**2))
    else:
        print("Нельзя поделить комплексные числа.")

def matplot(Z = Z):
    fig, ax = plt.subplots(1, 1, figsize =(7,7))
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xlabel("x")
    ax.set_ylabel("y")


    cc = ConjugateComplex()
    dc = DivisionComplex((1,0), Z)
    
    ax.plot((0,cc[1]), linestyle=":")
    ax.scatter(0, 0, label=u"0", s = 30, c = 'red')
    ax.scatter(Z[0], Z[1], s = 30,label=u"Z", c = 'green')
    ax.scatter(cc[0], cc[1], label=u"$\overline{Z}$", s = 30, c = 'blue')
    ax.scatter(dc[0], dc[1], label=u"$1/{Z}$", s = 30, c = 'orange')
    

    ax.set_axisbelow(True)
    ax.set_title('Комплексное число Z, сопряженное к нему, обратное и 0')
    ax.grid(True)
    ax.legend(loc="best", frameon=False)

    plt.show()

if __name__ == "__main__":
    matplot()
 
    


    