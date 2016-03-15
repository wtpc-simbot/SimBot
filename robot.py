'''
Aca tenemos a HAL
'''
from estrategia import Estrategia
from ambiente import Ambiente

class Robot():
    '''
    '''
    def __init__(self, orientacion, posicion, estrategia, ambiente):
        '''
		Inicializa el objeto Robot con su posicion, orientacion y un objeto estrategia asociado
        '''
		self.mi_estrategia = estrategia		
		self.mi_ambiente = ambiente        
		self.giroscopo = orientacion
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

    def mover(self, pasos):
         '''
        Esto usa la estrategia para una rapida solucion
		Sin retorno, actualiza la posicion del objeto
		Quizas deba agregar un chequeo de las orientaciones y de la poscion dentro del ambiente
         '''
		self.posicion[0] + pasos * self.giroscopo[0]
		self.posicion[1] + pasos * self.giroscopo[1]     
  
		self.historia_posiciones.append(self.posicion)
		# self.bateria -= 5
		# if self.bateria == 0:
		#	print("Me quede sin bateria")
		# apagar robot (puede ser una llamada a un metodo especifico) 

    def sensar(self):
         '''
        SOLO sensa para adelante y toma de ambientes la distancia al proximo obstaculo o limite en la orientacion actual	
		Devuelve el numero entero de pasos posibles hacia adelante
         '''
		return self.mi_ambiente.eco(self.posicion, self.giroscopo)
			
    def llamar_estrategia(self):
        '''
        Envia estado actual a estrategia para recibir una orden. Estrategia ejecutara las funciones mover, sensar y girar
        '''
		self.mi_estrategia.decidir(posicion, giroscopo, historia_posiciones)
		# eventualmente pasar la carga actual de la bateria
        
