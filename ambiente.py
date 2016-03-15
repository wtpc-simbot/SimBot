'''
ACA vive todo
'''

import numpy as np 
class Ambiente():

    def __init__(self,entrada,salida,tamano_x,tamano_y,cual_ambiente):
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

    def visualizar(self):
        '''
        TODO: hacer visualizacion
        hacer gif de la visualizacion
        visualizar en paralaro (multithreding)
        '''
        pass
    
    def eco(self, posicion, orientacion): 
        '''
        Devuelve True si en el proximo movimiento se encuentra una pared, sino False.
        '''
        if self.matriz[tuple(posicion + orientacion)] == 1:
            return True
        else:
            return False

            
    def estoy_fuera(self, posicion):
        '''
        Comprueba si salio
        '''
        # SOLUCION SUPER FEA TODO: algo mas lindo
        if posicion[0] == self.salida[0] and posicion[1] == self.salida[1]:
            return True
        else:
            return False

    