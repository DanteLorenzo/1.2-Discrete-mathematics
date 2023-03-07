import matplotlib.pyplot as plt
import numpy as np

def SumComplex(z1, z2):
    return (z1[0] + z2[0], z1[1] + z2[1])
def DifferenceComplex(z1, z2):
    return (z1[0] - z2[0], z1[1] - z2[1])
def MultiplicationComplex(z1, z2):
    return (z1[0]*z2[0] - z1[1]*z2[1], z1[1]*z2[0] + z1[0]*z2[1])
def DivisionComplex(z1, z2):
    if (z2[0] != 0) and (z2[0] != 0):
        return ((z1[0]*z2[0] + z1[1]*z2[1])/(z2[0]**2 + z2[1]**2), (z1[1]*z2[0] - z1[0]*z2[1])/(z2[0]**2 + z2[1]**2))
    else:
        print("Нельзя поделить комплексные числа.")
    
if __name__ == "__main__":
    N = 13
    Z1 = (1, -1.5)
    Z2 = (Z1[0] + 0.1*N, Z1[1] - 0.1*N)
    
    print(f"z1 = {Z1[0]} + ({Z1[1]}i)")
    print(f"z2 = {Z2[0]} + ({Z2[1]}i)")

    print(f"z1 + z2 = {SumComplex(Z1, Z2)[0]} + ({SumComplex(Z1, Z2)[1]}i)")
    print(f"z1 - z2 = {DifferenceComplex(Z1, Z2)[0]} + ({DifferenceComplex(Z1, Z2)[1]}i)")
    print(f"z1 * z2 = {MultiplicationComplex(Z1, Z2)[0]} + ({MultiplicationComplex(Z1, Z2)[1]}i)")
    print(f"z1 / z2 = {DivisionComplex(Z1, Z2)[0]} + ({DivisionComplex(Z1, Z2)[1]}i)")
    