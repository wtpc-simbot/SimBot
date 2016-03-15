'''
ACA vive todo
'''
from obstaculo import Obstaculo
from robot import Robot

class Ambiente():

    def __init__(self):
        '''
        '''
        self.entrada = entrada
        self.salida = salida
        self.tamano_x = tamano_x
        self.tamano_y = tamano_y
        self.obstaculos = obstaculos #Hacen falta los obtaculos?
        self.robot = robot
        self.generar_ambiente((self.tamano_x, self.tamano_y),
                              self.entrada, self.salida)
        pass

        def generar_ambiente(self, dimenciones, entrada, salida,
                             algoritmo_de_generacion):
        '''
        Genera donde se va a guardar la ubicacion de los
        obstaculos y del robot (posiblemente una matriz de tamano
        dimenciones, donde entrada y salida tienen la forma [x1, y1] ambos)
        Se podria tener varios algoritmos o templates para usar.
        '''
        pass

    def chequear_solucion(self):
        '''
        Comprueba que tenga solucion
        TODO: Poder chequear cosas particulares, la
        existencia de varios caminos por ejemplo,
        la dificultad del laberinto.
        '''
        pass

    def visualizar(self):
        '''
        TODO: hacer visualizacion
        hacer gif de la visualizacion
        visualizar en paralaro (multithreding)
        '''
        pass



    