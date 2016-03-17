'''
Un personaje que en sus tiempos libre mata minutoruos
'''

import numpy as np
from estrategia import Estrategia
from random import random
from ..robot import Robot
from utilidades import proximo_paso_en_historial

class Perseo(Estrategia):

    def __init__(self):
        #self.caminos = []
        self.camino_actual = []

    
    def decidir(self, robot, un_ambiente):
        self.robot = robot

        if self.robot.sensar(un_ambiente) != 0 and not proximo_paso_en_historial(robot):
            self.robot.mover(un_ambiente)
            self.camino_actual.append(list(self.robot.posicion))
        else:
            self.robot.rotar("izquierda")

        if self.robot.sensar(un_ambiente) != 0 and not proximo_paso_en_historial(robot):
            self.robot.mover(un_ambiente)
            self.camino_actual.append(list(self.robot.posicion))
        else:
            self.robot.rotar("izquierda")
            self.robot.rotar("izquierda")

        if self.robot.sensar(un_ambiente) != 0 and not proximo_paso_en_historial(robot):
            self.robot.mover(un_ambiente)
            self.camino_actual.append(list(self.robot.posicion))
        else:
            ultima_posicion = np.array(self.camino_actual.pop())
            if ultima_posicion[0] == self.robot.posicion[0] and \
               ultima_posicion[1] == self.robot.posicion[1]:
                pass
            else:
                orientacion_buscada = ultima_posicion - self.robot.posicion
                while orientacion_buscada[0] != self.robot.giroscopo[0] and orientacion_buscada[1] != self.robot.giroscopo[1]:
                    self.robot.rotar("derecha")

                self.robot.mover(un_ambiente)