'''
Camina siguiendo una pared (a la izquierda)
'''

from estrategia import Estrategia
from random import random

class Buscador_por_izquierda(Estrategia):

    def decidir(self, robot,un_ambiente):
        self.robot = robot


        self.robot.rotar("izquierda")        
        sensar_izquierda = self.robot.sensar(un_ambiente)       
        if sensar_izquierda > 0:
            self.robot.mover(un_ambiente)
        else:
            self.robot.rotar("derecha")
            sensar_adelante = self.robot.sensar(un_ambiente)       
            if sensar_adelante > 0:
                self.robot.mover(un_ambiente)
            else:
                self.robot.rotar("derecha")
