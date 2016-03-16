'''
Camina siguiendo una pared (a la derecha)
'''

from estrategia import Estrategia

class Buscador_por_derecha(Estrategia):

    def decidir(self, robot,un_ambiente):
        self.robot = robot

        if self.robot.sensar(un_ambiente) == 0:
            self.robot.rotar("izquierda")
            self.robot.mover(un_ambiente)
            
        else:
            self.robot.rotar("derecha")
            if self.robot.sensar(un_ambiente) == 0:
                self.robot.rotar("izquierda")
                self.robot.mover(un_ambiente)
            else:
                self.robot.mover(un_ambiente)
            