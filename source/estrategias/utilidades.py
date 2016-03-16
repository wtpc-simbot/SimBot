'''
Algunas funciones que facilitan a hora de salir del laberinto
'''

def proximo_paso_en_historial(robot):
    if list(robot.posicion + robot.giroscopo) in \
       robot.historia_posiciones:
        return True
    else:
        return False