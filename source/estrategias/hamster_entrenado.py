'''
Toma la estrategia de un hamster caminando para cualquier
lugar, pero evita los lugares donde ya estuvo.
'''

from estrategia import Estrategia
from utilidades import proximo_paso_en_historial

from random import random

class Hamster_Entrenado(Estrategia):

    def estrategia(self, robot):
        self.robot = robot
        numero = random()

        movimiento_posible = False
        
        while not movimiento_posible:

            if numero < 1/3.:
                self.robot.rotar("izquierda")
                if proximo_paso_en_historial(self.robot):
                    pass
                else:
                    self.robot.mover()
                    movimiento_posible = True
                #doblar a la izquierda y caminar
            elif numero > 1/3. and numero < 2/3.:
                self.robot.rotar("derecha")
                if proximo_paso_en_historial(self.robot):
                    pass
                else:            
                    self.robot.mover()
                    movimiento_posible = True
                #doblar a la derecha y caminar
            else:
                if proximo_paso_en_historial(self.robot):
                    pass
                else:                
                    self.robot.mover()
                    movimiento_posible = True
            