'''
Esta es una clase de laberinto
'''
import numpy as np

class Laberinto():

    def __init__(self, entrada, salida, tamano_x, tamano_y):

        self.entrada = entrada 
        self.salida = salida   
        self.tamano_x = tamano_x 
        self.tamano_y = tamano_y
        
    def hacer(self):
            
        size = (self.tamano_x,self.tamano_y)
        matriz = np.zeros(size)
                    
        matriz[0:self.tamano_x,0] = 1
        matriz[0:self.tamano_x,self.tamano_y-1] = 1
        matriz[0,0:self.tamano_y] = 1
        matriz[self.tamano_x-1,0:self.tamano_y] = 1
        matriz[3,2:9] = 1
        matriz[6,0:8] = 1
        matriz[4:6,5] = 1

        matriz[self.entrada] = 2
        matriz[self.salida] = 3

        return matriz