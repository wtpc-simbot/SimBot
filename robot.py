'''
Aca tenemos a HAL
'''
from estrategia import Estrategia

class Robot():
    '''
    '''
    def __init__(self,posicion,orientacion):
        '''
        '''
        self.giroscopo = orientacion
        self.posicion = posicion
        #self.estrategia = estrategia.Estrategia 
        self.historia_posiciones = []
        self.historia_acciones = []
        pass

    def rotar(self):
        '''

        '''
        pass
        
    def mover(self):
         '''
         Esto usa la estrategia para una rapida solucion
         '''
         pass

    def sensar(self):
         '''
         SOLO sensa para adelante
         '''
         pass

    def proximo_paso(self):
        '''
        Dado el estado actual decido que hacer
        '''
        pass
