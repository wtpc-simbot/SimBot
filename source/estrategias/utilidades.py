'''
Algunas funciones que facilitan a hora de salir del laberinto
'''

def proximo_paso_en_historial(robot):
    """
    Indica si el robot ya paso por esas coordenadas.
    """
    if list(robot.posicion + robot.giroscopo) in robot.historia_posiciones:
        return True
    else:
        return False

def posicion_ultimo_giro(robot):
	"""
	Devuelve las coordenadas de posicion antes del ultimo giro
	"""
	acciones = len(robot.historia_acciones)
	contador = 0
	
	while robot.historia_acciones[acciones] != "l" and robot.historia_acciones[acciones] != "r":
		if robot.historia_acciones[acciones] == "f":
			contador += 1
		acciones -= 1
	ret = robot.historia_posiciones[-(acciones+1)]
	return ret
	"""
	Alternativa:
	for i in range(acciones,0,-1):
		if robot.historia_acciones[acciones] == "f"
			contador += 1
		else:
			if robot.historia_acciones[accones] != "s":
				return robot.historia_posiciones[-(i+1)]
	"""

def retorno_ultimo_giro(robot, ambiente):
    """
    Retorna al robot a su posicion antes del ultimo giro en su trayectoria (ignora los giros que haya hecho luego del ultimo paso realizado)
    """
    # acciones sera el indice para ubicar el ultimo elemento del historial de acciones
    acciones = len(robot.historia_acciones)
	# Indica que hasta el momento el robot no fue rotado desde su ultimo giro
    robot_rotado == False
	# Busca en el historial de acciones si hubo algun giro luego del ultimo movimiento y lo revierte. Ignora los sensados.
    while robot.historia_acciones[acciones] != "f":
        if robot.historia_acciones[acciones] == "s":
            acciones -= 1   
        else:
            if robot.historia_acciones[acciones] == "r":
                robot.rotar("izquierda") 
            if robot.historia_acciones[acciones] == "l":
                robot.rotar("derecha")
            contador -= 1
            robot_rotado == True
	# Si no deshizo ningun giro hasta ahora, hay que girar el robot 180 grados para poder deshacer los ultimos pasos.
	if not robot_rotado:
	    robot.rotar("derecha")
	    robot.rotar("derecha")
    # Avanza hacia atras hasta hallar el ultimo giro en el historial.
    while robot.historia_acciones[acciones] != "l" and robot.historia_acciones[acciones] != "r":
        if robot.historia_acciones[aciones] == "s":
            acciones -= 1
        else:
        # chequear como paso ambiente
            robot.mover(ambiente)
            acciones -= 1
    # Deshace el ultimo giro.
    if robot.historia_acciones[acciones] == "r":
        robot.rotar("izquierda") 
    if robot.historia_acciones[acciones] == "l":
        robot.rotar("derecha")      
    
        
           

