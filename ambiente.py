'''
ACA vive todo

INSTALAR python-gasp

'''


import numpy as np 
from gasp import *
import time
class Ambiente():

    def __init__(self,entrada,salida,tamano_x,tamano_y,robot,cual_ambiente):
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
        self.entrada = entrada 
        self.salida = salida   
        self.tamano_x = tamano_x 
        self.tamano_y = tamano_y
        #self.obstaculos = obstaculos #Hacen falta los obtaculos?
        self.robot = robot
        self.matriz = self.generar_ambiente(cual_ambiente)


    def generar_ambiente(self,cual_ambiente): #, dimensiones, entrada, salida
            #,algoritmo_de_generacion):
        '''
        Genera donde se va a guardar la ubicacion de los
        obstaculos y del robot (posiblemente una matriz de tamano
        dimensiones, donde entrada y salida tienen la forma [x1, y1] ambos)
        Se podria tener varios algoritmos o templates para usar.
        '''
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

        if matriz[tuple(self.robot.posicion)]==1:
            raise Exception(  "OOOPS el robot esta sobre una pared..." )            

        return matriz            

    def chequear_solucion(self):
        '''
        Comprueba que tenga solucion, que se pueda ir caminando desde la 
                entrada a la salida
        '''        
        while True:
            aux=0
            tiene_solucion = 0
            for i in xrange(1,self.tamano_x-1):
                for j in xrange(1,self.tamano_y-1):
                    if  self.matriz[i,j]==2:
                        #chequeo si llegue a la solucion
                        if self.matriz[i,j+1]==3:
                            tiene_solucion = 1 
                        if self.matriz[i,j+1]==3:
                            tiene_solucion = 1 
                        if self.matriz[i,j+1]==3:
                            tiene_solucion = 1 
                        if self.matriz[i,j+1]==3:
                            tiene_solucion = 1 

                        #avanzo un paso para todos lados
                        if self.matriz[i,j+1]==0:
                            aux += 1
                            self.matriz[i,j+1] = 2
                        if self.matriz[i,j-1]==0:
                            aux += 1
                            self.matriz[i,j-1] = 2
                        if self.matriz[i+1,j]==0:
                            aux += 1
                            self.matriz[i+1,j] = 2
                        if self.matriz[i-1,j]==0:
                            aux += 1
                            self.matriz[i-1,j] = 2
            #print self.matriz
            if aux == 0:
                break
            if tiene_solucion == 1:
                break
        return tiene_solucion                

    def sensar(self): 
        '''
        Devuelve la cantidad de casillas libres por delante del robot
        '''
        distancia = 0
        posactual = self.robot.posicion  + self.robot.giroscopo
        #print posactual , self.matriz[tuple(posactual)]
        while self.matriz[tuple(posactual)] != 1:
            #print posactual
            posactual += self.robot.giroscopo
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



    
