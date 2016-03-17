'''
Camina siguiendo una pared (a la derecha)
'''

from estrategia import Estrategia
from utilidades import proximo_paso_en_historial
from random import random

class Buscador_por_derecha(Estrategia):

    def decidir(self, robot,un_ambiente):
        self.robot = robot

        if self.robot.sensar(un_ambiente) == 0:
            self.robot.rotar("izquierda")
            if proximo_paso_en_historial(self.robot):
                rotacion_aleatoria(robot)
            else:           
                self.robot.mover(un_ambiente)
            
        else:
            self.robot.rotar("derecha")
            if self.robot.sensar(un_ambiente) == 0:
                self.robot.rotar("izquierda")
                if proximo_paso_en_historial(self.robot):
                    rotacion_aleatoria(robot)
                else:               
                    self.robot.mover(un_ambiente)
            else:
                if proximo_paso_en_historial(self.robot):
                    rotacion_aleatoria(robot)
                else:               
                    self.robot.mover(un_ambiente)
 
def rotacion_aleatoria(robot):
    numero = random()
    if numero > 1/2.:
        robot.rotar("izquierda")
    else:
        robot.rotar("derecha")                    
