'''
Aca tenemos a HAL
'''
from estrategias.estrategia import Estrategia

class Robot():
    '''
    '''
    def __init__(self, orientacion, posicion, estrategia):
        '''
		Inicializa el objeto Robot con su posicion, orientacion y un objeto Estrategia asociado.
		Parametros
		----------
		orientacion: List(int,int)
			Lista con la orientacion (x,y) del Robot en la matriz del Ambiente (laberinto).
		posicion: List(int,int)
			Lista correspondiente a las orientaciones "arriba" (0,1), "abajo" (0,-1), "izquierda" (-1,0) y "derecha" (1,0)
		estrategia: objeto Estrategia
			Objeto Estrategia inicializado por main que decidira las acciones del Robot.
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
		Cambia la orientacion del Robot.
		Parametros
		----------
		giro: str
			Valores posibles: "derecha" e "izquierda"
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
		Cambia la posicion del Robot en el Ambiente (laberinto). Agrega el movimiento a la lista historia_posiciones.
		Parametros
		----------
		un_ambiente: objeto Ambiente
			Instancia del objeto Ambiente creada por main. Es el laberinto en el cual se mueve el robot
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
		Obtiene la distancia del robot al proximo obstaculo del laberinto en la orientacion actual. 
		Parametros
		----------
		un_ambiente: objeto Ambiente
			Instancia del objeto Ambiente creada por main. Es el laberinto en el cual se mueve el robot.		
		Devuelve
		--------
		un_ambiente.eco(): int
			Distancia (en pasos) al proximo obstaculo del laberinto.
         '''
         return un_ambiente.eco()         
         
    def salir_del_laberinto(self,un_ambiente):
        '''
		Envia a Estrategia el estado actual (posicion y orientacion) del robot y la distancia al proximo obstaculo obtenida por su sensor y recibe instrucciones para la proxima accion.        
		Parametros
		-----------
		un_ambiente: objeto Ambiente
			Instancia del objeto Ambiente creada por main. Es el laberinto en el cual se mueve el robot.
        '''
        print self.posicion , self.giroscopo , self.sensar(un_ambiente)
        while not un_ambiente.estoy_fuera(self.posicion):            
            self.mi_estrategia.decidir(self,un_ambiente)
            print self.posicion , self.giroscopo , self.sensar(un_ambiente)
        # eventualmente pasar la carga actual de la bateria

