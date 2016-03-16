'''
ACA vive todo

INSTALAR python-gasp

'''


import numpy as np 
from gasp import *
import time

class Ambiente():

    def __init__(self, entrada, salida, tamano_x, tamano_y, robot, 
                 cual_ambiente):
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

        # Quitado el robot de ambiente
        #if matriz[tuple(self.robot.posicion)]==1:
        #    raise Exception(  "OOOPS el robot esta sobre una pared..." )            
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

    def eco(self): 
        '''
        Devuelve la cantidad de casillas libres por delante del robot
        '''
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
                if self.matriz[f][c] == 0:
                    Image("./img/grass.png", (w, h))
                elif self.matriz[f][c] == 1:
                    Image("./img/bloque.png", (w, h))
                elif self.matriz[f][c] == 2:
                    Image("./img/in.png", (w, h))
                    Image("./img/robot_up.png", (w, h))
                elif self.matriz[f][c] == 3:
                    Image("./img/grass.png", (w, h))
                    Image("./img/exit.png", (w, h))
                w += 32
            h -= 32
        time.sleep(2)
        
    def actualizar(self, posViejaRobot, posNuevaRobot, orientacion):
        '''
        Funcion que muestra por pantalla el recorrido del robot
        atraves del laberinto, hasta que llega a la salida
        
        orientacion
        (-1,0) abajo 
        (0,1) derecha
        (1,0) arriba
        (0,-1) izquierda
        
        
        ENTRADA:
			posicion:  punto en donde se encuentra el robot
        SALIDA:
			Imagen por pantalla
        '''
        '''
        if orientacion[0] == 1 and orientacion[1] == 0:
            imagen_orientacion = "./img/robot_down.png"
        elif orientacion[0] == 0 and orientacion[1] == 1:
            imagen_orientacion = "./img/robot_up.png"
        elif orientacion[0] == -1 and orientacion[1] == 0:
            imagen_orientacion = "./img/robot_right.png"
        elif orientacion[0] == 0 and orientacion[1] == -1:
            imagen_orientacion = "./img/robot_left.png"
        '''
        imagen_orientacion = "./img/robot_up.png"
        Image(imagen_orientacion, (32*posViejaRobot[1]+16, (self.tamano_y*32)-16-32*posViejaRobot[0])) 
        
        time.sleep(.5)
        if posViejaRobot[0] == self.entrada[0] and posViejaRobot[1] == self.entrada[1]:
            Image("./img/in.png", (32*posViejaRobot[1]+16, (self.tamano_y*32)-16-32*posViejaRobot[0])) 
            Image(imagen_orientacion, (32*posNuevaRobot[1]+16, (self.tamano_y*32)-16-32*posNuevaRobot[0]))
            
        elif posNuevaRobot[0] == self.salida[0] and  posNuevaRobot[1] == self.salida[1]:
            Image("./img/grass.png", (32*posViejaRobot[1]+16, (self.tamano_y*32)-16-32*posViejaRobot[0]))
            Image(imagen_orientacion, (32*posNuevaRobot[1]+16, (self.tamano_y*32)-16-32*posNuevaRobot[0]))
            time.sleep(1)
            Image("./img/grass.png", (32*posNuevaRobot[1]+16, (self.tamano_y*32)-16-32*posNuevaRobot[0]))
            Image("./img/ganar.png", (int(((self.tamano_y*32)-16)/2),int(((self.tamano_y*32)-16)/2)))
            time.sleep(5)            
        elif posViejaRobot[0] == posNuevaRobot[0] or posViejaRobot[1] == posNuevaRobot[1]:
            Image("./img/grass.png", (32*posViejaRobot[1]+16, (self.tamano_y*32)-16-32*posViejaRobot[0]))
            Image(imagen_orientacion, (32*posNuevaRobot[1]+16, (self.tamano_y*32)-16-32*posNuevaRobot[0]))
            
        time.sleep(.1)
        
    def estoy_fuera(self, posicion):
        '''
        Comprueba si salio
        '''
        # SOLUCION SUPER FEA TODO: algo mas lindo
        if posicion[0] == self.salida[0] and posicion[1] == self.salida[1]:
            print "Libertad!!!"
            return True
        else:
            return False


    
