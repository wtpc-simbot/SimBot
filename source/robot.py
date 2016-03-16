'''
Aca tenemos a HAL
'''
from estrategias.estrategia import Estrategia

class Robot():
    '''
    '''
    def __init__(self, orientacion, posicion, estrategia):
        '''
		Inicializa el objeto Robot con su posicion, orientacion y un objeto estrategia asociado
        '''
        #self.mi_ambiente = ambiente        
        self.giroscopo = orientacion
        # TODO hacer la posicion un array
        self.posicion = posicion
        self.historia_posiciones = []
        self.historia_acciones = []
        """
		TODO: agregar una bateria que se vaya consumiendo con los movimientos y en menor medida con los giros
		self.bateria = carga
		"""
        # asumo que estrategia fue inicializada por el main
        self.mi_estrategia = estrategia

    def rotar(self, giro):
        '''
		Recibe un int giro de estrategia y actualiza la orientacion del giroscopo
		Sin retorno, solo actualiza la orientacion, en grados
        '''
        if giro == "derecha":
			a = self.giroscopo[0]
			self.giroscopo[0] = self.giroscopo[1]
			self.giroscopo[1] = -a
		
        if giro == "izquierda":
			a = self.giroscopo[1]
			self.giroscopo[1] = self.giroscopo[0]
			self.giroscopo[0] = -a
			
        #self.historia_acciones.append(self.giroscopo)

    def mover(self,un_ambiente):
         '''
        Esto usa la estrategia para una rapida solucion
		Sin retorno, actualiza la posicion del objeto
		Quizas deba agregar un chequeo de las orientaciones y de la poscion dentro del ambiente
         '''
         if self.sensar(un_ambiente) != 0:
             self.posicion[0] += self.giroscopo[0]
             self.posicion[1] += self.giroscopo[1]     
         else:
             # Choca contra la pared
             pass
             
         self.historia_posiciones.append(self.posicion)
         
         # self.bateria -= 5
         # if self.bateria == 0:
         #	print("Me quede sin bateria")
         # apagar robot (puede ser una llamada a un metodo especifico) 

    def sensar(self,un_ambiente):        
         '''
         SOLO sensa para adelante y toma de ambientes la distancia al proximo obstaculo o limite en la orientacion actual	
	   Devuelve el numero entero de pasos posibles hacia adelante
         TODO: Contemplar el caso de que sense la entrado o la salida.
         '''
         return un_ambiente.eco()         
         
    def salir_del_laberinto(self,un_ambiente):
        '''
        Envia estado actual a estrategia para recibir una orden. Estrategia ejecutara las funciones mover, sensar y girar
        TODO: Comprobar estado de la bateria, en caso de que se termine romper el while.
        '''
        print self.posicion , self.giroscopo , self.sensar(un_ambiente)
        while not un_ambiente.estoy_fuera(self.posicion):            
            self.mi_estrategia.decidir(self,un_ambiente)
            print self.posicion , self.giroscopo , self.sensar(un_ambiente)
        # eventualmente pasar la carga actual de la bateria
        
