import numpy as np

def imprimir():
    with open('k.py', 'w') as f:
        f.write('constantes = [')
        for kp in np.arange(0.1, 0.6, 0.1):
            for ki in np.arange(0.1, 0.6, 0.1):
                for kd in np.arange(0.1, 0.6, 0.1):
                    f.write("[{0}, {1}, {2}],\n".format(kp, ki, kd))
        f.write(']')

from k import *

print(constantes[5])
print(constantes[10])
print(constantes[15])
print(constantes[20])
print(constantes[39])
print(constantes[44])
print(constantes[49])
print(constantes[54])
print(constantes[61])
print(constantes[66])
print(constantes[71])
print(constantes[76])
print(constantes[81])
print(constantes[86])
print(constantes[91])
print(constantes[106])
