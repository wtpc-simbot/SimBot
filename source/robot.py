'''
Aca tenemos a HAL
'''

class Robot():
    '''
    Clase robot
    '''
    
    def __init__(self, orientacion, posicion, estrategia, carga_inicial):
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
        self.giroscopo = orientacion
        # TODO hacer la posicion un array
        self.posicion = posicion
        self.historia_posiciones = []
        self.historia_acciones = []
        self.carga_inicial = carga_inicial
        self.bateria = carga_inicial
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
			self.historia_acciones.append('r')		
        if giro == "izquierda":
			a = self.giroscopo[1]
			self.giroscopo[1] = self.giroscopo[0]
			self.giroscopo[0] = -a
			self.historia_acciones.append('l')
        self.consumo_bateria('rotar')
       

    def mover(self,un_ambiente):
         '''
		Cambia la posicion del Robot en el Ambiente (laberinto). Agrega el movimiento a la lista historia_posiciones.
		Parametros
		----------
		un_ambiente: objeto Ambiente
			Instancia del objeto Ambiente creada por main. Es el laberinto en el cual se mueve el robot
         #Esto va?
        Esto usa la estrategia para una rapida solucion
		Sin retorno, actualiza la posicion del objeto
		Quizas deba agregar un chequeo de las orientaciones y de la poscion dentro del ambiente
         '''
         
         if self.sensar(un_ambiente) != 0:
             self.posicion[0] += self.giroscopo[0]
             self.posicion[1] += self.giroscopo[1]
             self.consumo_bateria('mover')
             self.historia_acciones.append('f')
         else:
             # Choca contra la pared
             self.consumo_bateria('chocar')
             self.historia_acciones.append('x')
             pass
             
         self.historia_posiciones.append(list(self.posicion))
         
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
         self.consumo_bateria('sensar')
         self.historia_acciones.append('s')

         return un_ambiente.eco()         
         
    def salir_del_laberinto(self,un_ambiente):
        '''
		Envia a Estrategia el estado actual (posicion y orientacion) del robot y
        la distancia al proximo obstaculo obtenida por su sensor y recibe
        instrucciones para la proxima accion.
        
		Parametros
		-----------
		un_ambiente: objeto Ambiente
			Instancia del objeto Ambiente creada por main. Es el laberinto en el
        cual se mueve el robot.
        '''

        posicion_sin_avanzar=self.posicion.copy()
        giro = self.giroscopo.copy()
        while not un_ambiente.estoy_fuera() and \
              (self.carga_inicial == 0 or self.bateria > 0):            
            self.mi_estrategia.decidir(self,un_ambiente)
            #un_ambiente.actualizar(posicion_sin_avanzar, self.posicion, self.giroscopo)
            posicion_sin_avanzar=self.posicion.copy()
            giro = self.giroscopo.copy()
    
    def consumo_bateria(self,accion):
        if self.carga_inicial > 0:            
            gasto_por_mover   = 2
            gasto_por_rotar   = 1
            gasto_por_chocar  = 4
            gasto_por_sensar  = 1 
            if accion == 'rotar':
                 self.bateria -= gasto_por_rotar
            elif accion == 'mover':
                 self.bateria -= gasto_por_mover
            elif accion == 'chocar':
                 self.bateria -= gasto_por_chocar
            elif accion == 'sensar':
                 self.bateria -= gasto_por_sensar
            if self.bateria <= 0:
                print 'Me quede sin bateria!!!'

