'''
Toma la estrategia de un hamster caminando para cualquier lugar
'''

from estrategia import Estrategia
from random import random

class Hamster(Estrategia):

    def estrategia(self, robot):
        self.robot = robot
        numero = random()

        if numero < 1/3.:
            self.robot.rotar("izquierda")
            self.robot.mover()
            #doblar a la izquierda y caminar
        elif numero > 1/3. and numero < 2/3.:
            self.robot.rotar("derecha")
            self.robot.mover()
            #doblar a la derecha y caminar
        else:
            self.robot.mover()
            