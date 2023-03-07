import math
import matplotlib.pyplot as plt
import numpy as np


Z = (1, -1.5)
N = 13

def PrintGeometricForm():
    print('Geometric form of complex number:')
    print(f'z = {Module()} * (cos({Argument()}) + i * sin({Argument()}))')

def PrintExponentialForm():
    print('Exponential form of complex number:')
    print(f'z = {Module()} * e^({Argument()} i)')

def PrintRootofaComplexNumber():
    re, im = RootofaComplexNumber()
    print("Root of a complex number:")
    for i in range(len(re)):
        print(f"Z[{i}] = {re[i]} + i*{im[i]}")

def Module(z = Z):
    return (math.sqrt(math.pow(Z[0], 2) + math.pow(Z[1], 2)))

def Argument(z = Z):
    if z[0] == 0:
        if z[1] < 0:
            return (-math.pi/2)
        elif z[1] > 0:
            return (math.pi/2)
    elif z[0] < 0:
        if z[1] >= 0:
            return (math.pi + math.atan(z[1]/z[0]))
        else:
            return (-math.pi + math.atan(z[1]/z[0]))
    else:
        return (math.atan(z[1]/z[0]))
    
def RootofaComplexNumber(z = Z, n = N + 5):
    result_re = [] 
    result_im = []

    for k in range(n):
        result_re.append(math.pow(Module(), (1/n)) * math.cos((Argument() + 2 * math.pi * k)/n))
        result_im.append(math.pow(Module(), (1/n)) * math.sin((Argument() + 2 * math.pi * k)/n))
    return result_re, result_im

def matplot():
    fig, ax = plt.subplots(1, 1, figsize =(7,7))
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)

    re,im = RootofaComplexNumber()
    ax.scatter(x = Z[0], y = Z[1], label=u"Z", s = 10, c = 'red')
    ax.scatter(x = re, y = im, label=u"$\sqrt[18]{Z}$", s = 10, c = 'blue')

    ax.set_axisbelow(True)
    ax.set_title('Комплексное число Z и его корни')
    ax.grid(True)
    ax.legend(loc="best", frameon=False)

    plt.show()

if __name__ == "__main__":
    print(Module())
    print(Argument())
    PrintGeometricForm()
    PrintExponentialForm()
    PrintRootofaComplexNumber()
    matplot()
    
    
