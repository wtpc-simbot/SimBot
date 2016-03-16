'''
ACA vive todo

INSTALAR python-gasp

'''


import numpy as np 
from gasp import *
import time
from source.robot import Robot
from laberinto import Laberinto

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
        
        #self.entrada = entrada 
        #self.salida = salida   
        #self.tamano_x = tamano_x 
        #self.tamano_y = tamano_y
        self.robot = robot
        self.laberinto = laberinto
        self.matriz = self.laberinto.hacer()

    def generar_ambiente(self,cual_ambiente):
        """
        Genera la matriz, pone obstaculos y paredes con el siguiente codigo
            0 vacio
            1 paredes / obstaculos
            2 posicion de entrada
            3 posicion de salida            

        Parameters
        ----------
        cual_ambiente : int
            Un selector de laberintos predefinidos
            
        """
        size = (self.tamano_x,self.tamano_y)
        matriz = np.zeros(size)               

        if cual_ambiente==0:
            matriz[0:self.tamano_x,0] = 1
            matriz[0:self.tamano_x,self.tamano_y-1] = 1
            matriz[0,0:self.tamano_y] = 1
            matriz[self.tamano_x-1,0:self.tamano_y] = 1
            matriz[5,0:8] = 1
        elif cual_ambiente==1:        
            matriz[0:self.tamano_x,0] = 1
            matriz[0:self.tamano_x,self.tamano_y-1] = 1
            matriz[0,0:self.tamano_y] = 1
            matriz[self.tamano_x-1,0:self.tamano_y] = 1
            matriz[3,2:9] = 1
            matriz[6,0:8] = 1
        elif cual_ambiente==2:        
            matriz[0:self.tamano_x,0] = 1
            matriz[0:self.tamano_x,self.tamano_y-1] = 1
            matriz[0,0:self.tamano_y] = 1
            matriz[self.tamano_x-1,0:self.tamano_y] = 1
            matriz[3,2:9] = 1
            matriz[6,0:8] = 1
            matriz[4:6,5] = 1
        elif cual_ambiente==3:        
            matriz[0:self.tamano_x,0] = 1
            matriz[0:self.tamano_x,self.tamano_y-1] = 1
            matriz[0,0:self.tamano_y] = 1
            matriz[self.tamano_x-1,0:self.tamano_y] = 1
            matriz[1:9,4] = 1
        else:
            raise Exception(  "no conozco ese ambiente"  )
        
        #entrada = 2 y salida = 3
        matriz[self.entrada] = 2
        matriz[self.salida] = 3                   

        # Quitado el robot de ambiente
        #if matriz[tuple(self.robot.posicion)]==1:
        #    raise Exception(  "OOOPS el robot esta sobre una pared..." )            

        return matriz            
        

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
            #print una_matriz
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
        distancia = 0
        posicion_sensada = self.robot.posicion  + self.robot.giroscopo
        #print posicion_sensada , self.matriz[tuple(posicion_sensada)]
        while self.matriz[tuple(posicion_sensada)] != 1:
            #print posicion_sensada
            posicion_sensada += self.robot.giroscopo
            distancia += 1
        return distancia

    def visualizar(self):        
        '''
        Funcion que muestra por pantalla el laberinto
        
        ENTRADA:
			Ambiente
        SALIDA:
			Imagen por pantalla
        '''
        h = (self.tamano_y*32)-16
        for f in range(self.tamano_x):
            w = 16
            for c in range(self.tamano_y):
                if self.laberinto[f][c] == 0:
                    Image("grass.png", (w, h))
                elif self.matriz[f][c] == 1:
                    Image("bloque.png", (w, h))
                elif self.matriz[f][c] == 2:
                    Image("in.png", (w, h))
                    Image("robot.png", (w, h))
                elif self.matriz[f][c] == 3:
                    Image("grass.png", (w, h))
                    Image("exit.png", (w, h))
                w += 32
            h -= 32
        time.sleep(2)
        
    def actualizar(self, posViejaRobot, posNuevaRobot):
        '''
        Funcion que muestra por pantalla el recorrido del robot
        atraves del laberinto, hasta que llega a la salida
        
        ENTRADA:
			posicion:  punto en donde se encuentra el robot
        SALIDA:
			Imagen por pantalla
        '''
        
        if posViejaRobot == self.entrada:
            Image("in.png", (32*posViejaRobot[1]+16, (self.tamano_y*32)-16-32*posViejaRobot[0])) 
            Image("robot.png", (32*posNuevaRobot[1]+16, (self.tamano_y*32)-16-32*posNuevaRobot[0]))
        elif posNuevaRobot == self.salida:
            Image("grass.png", (32*posViejaRobot[1]+16, (self.tamano_y*32)-16-32*posViejaRobot[0]))
            Image("robot.png", (32*posNuevaRobot[1]+16, (self.tamano_y*32)-16-32*posNuevaRobot[0]))
            time.sleep(2)
            Image("grass.png", (32*posNuevaRobot[1]+16, (self.tamano_y*32)-16-32*posNuevaRobot[0]))
            Image("ganar.png", (int(((self.tamano_y*32)-16)/2),int(((self.tamano_y*32)-16)/2)))
            time.sleep(5)            
        else:
            Image("grass.png", (32*posViejaRobot[1]+16, (self.tamano_y*32)-16-32*posViejaRobot[0]))
            Image("robot.png", (32*posNuevaRobot[1]+16, (self.tamano_y*32)-16-32*posNuevaRobot[0]))
            
        time.sleep(1)

            
    def estoy_fuera(self):
        """
        Comprueba si la posicion actual del robot es la casilla de salida
        
        Returns
        -------    
        bool
            True si el robot esta en la salida, False si no.
        """
        if self.robot.posicion[0] == self.laberinto.salida[0] and self.robot.posicion[1] == self.laberinto.salida[1]:
            print "Libertad!!!"
            return True
        else:
            return False


    
