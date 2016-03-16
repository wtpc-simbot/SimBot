'''
Toma la estrategia de un hamster caminando para cualquier lugar
'''

from estrategia import Estrategia
from random import random
from ..robot import Robot


class Hamster(Estrategia):

    def decidir(self, robot,un_ambiente):
        self.robot = robot
        numero = random()

        if numero < 1/3.:
            self.robot.rotar("izquierda")
            self.robot.mover(un_ambiente)
            #doblar a la izquierda y caminar
        elif numero > 1/3. and numero < 2/3.:
            self.robot.rotar("derecha")
            self.robot.mover(un_ambiente)
            #doblar a la derecha y caminar
        else:
            self.robot.mover(un_ambiente)
            