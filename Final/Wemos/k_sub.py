import numpy as np

def imprimir():
    with open('k.py', 'w') as f:
        f.write('constantes = [')
        for kp in np.arange(0.1, 0.6, 0.1):
            for ki in np.arange(0.1, 0.6, 0.1):
                for kd in np.arange(0.1, 0.6, 0.1):
                    f.write("[{0}, {1}, {2}],\n".format(kp, ki, kd))
        f.write(']')

imprimir()
