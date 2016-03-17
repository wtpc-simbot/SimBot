'''
ACA vive todo

INSTALAR python-gasp

'''

import numpy as np
import grafico as gfc
from source.robot import Robot 
from time import sleep
from gasp import *

class Ambiente():

    def __init__(self, robot, laberinto):
        '''
        entrada: 2-tuple
        salida: 2-tuple
        tamano_x: tamano de la cancha
        tamano_y: tamano de la cancha
        robot: el robot que vive en este ambiente
        matriz: np.array de de tamano_x por tamano_y que tiene:
            0: vacio
            1: paredes / obstaculos
            2: entrada
            3: salida
        '''
        
        self.robot = robot
        self.laberinto = laberinto
        self.matriz = self.laberinto.hacer()

    def chequear_solucion(self):
        """
        Comprueba que tenga solucion, que se pueda ir caminando desde la 
                entrada a la salida
 
        Returns
        -------    
        bool
            True si se puede llegar de la entrada a la salida, False si no.
        """                
        una_matriz = self.matriz.copy()
        while True:
            aux=0
            tiene_solucion = 0
            for i in xrange(1,self.laberinto.tamano_x-1):
                for j in xrange(1,self.laberinto.tamano_y-1):
                    if  una_matriz[i,j]==2:
                        #chequeo si llegue a la solucion
                        if una_matriz[i,j+1]==3:
                            tiene_solucion = 1 
                        if una_matriz[i,j+1]==3:
                            tiene_solucion = 1 
                        if una_matriz[i,j+1]==3:
                            tiene_solucion = 1 
                        if una_matriz[i,j+1]==3:
                            tiene_solucion = 1 

                        #avanzo un paso para todos lados
                        if una_matriz[i,j+1]==0:
                            aux += 1
                            una_matriz[i,j+1] = 2
                            
                        if una_matriz[i,j-1]==0:
                            aux += 1
                            una_matriz[i,j-1] = 2

                        if una_matriz[i+1,j]==0:
                            aux += 1
                            una_matriz[i+1,j] = 2

                        if una_matriz[i-1,j]==0:
                            aux += 1
                            una_matriz[i-1,j] = 2
            if aux == 0:
                break
            if tiene_solucion == 1:
                break
        return tiene_solucion  
        
   
    def eco(self): 
        """
        Devuelve la cantidad de casillas libres por delante del robot
 
        Returns
        -------    
        int
            cantidad de casillas libres delante del robot (0 si esta mirando 
            la pared).
        """            
        '''
        distancia = 0
        posicion_sensada = self.robot.posicion  + self.robot.giroscopo
        #print posicion_sensada , self.matriz[tuple(posicion_sensada)]
        '''
        distancia = 0
        posicion_actual = self.robot.posicion.copy()
        posicion_sensada = self.robot.posicion  + self.robot.giroscopo
        gfc.visualizar_mirada(posicion_actual, posicion_sensada,self.robot.giroscopo)
        while self.matriz[tuple(posicion_sensada)] != 1:
            posicion_sensada += self.robot.giroscopo
            distancia += 1
       
        return distancia

    def estoy_fuera(self):
        """
        Comprueba si la posicion actual del robot es la casilla de salida
        
        Returns
        -------    
        bool
            True si el robot esta en la salida, False si no.
        """
        if self.robot.posicion[0] == self.laberinto.salida[0] and \
           self.robot.posicion[1] == self.laberinto.salida[1]:
            print "Libertad!!!"
            return True
        else:
            return False


    
