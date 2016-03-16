'''
Camina siguiendo una pared (a la derecha)
'''

from estrategia import Estrategia

class Buscador_por_derecha(Estrategia):

    def estrategia(self, robot):
        self.robot = robot

        if self.robot.sensar() == 0:
            self.robot.rotar("izquierda")
            self.robot.mover()
            
        else:
            self.robot.rotar("derecha")
            if self.robot.sensar() == 0:
                self.robot.rotar("izquierda")
                self.robot.mover()
            else:
                self.robot.mover()
            