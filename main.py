import numpy as np
from gasp import *
from source.ambiente import Ambiente
from source.robot import Robot
from source.laberintos.deep_first_search import Laberinto

from source.estrategias.hamster import Hamster

tamano_x, tamano_y = (15,15)
entrada = (1,1)
salida = (tamano_x-2,tamano_y-2)
pos_robot = np.array(entrada)
ori_robot = np.array((0,1))

hamster = Hamster()
carga_inicial = 1000000

robot = Robot(ori_robot, pos_robot, hamster, carga_inicial)
laberinto = Laberinto(entrada, salida, tamano_x, tamano_y)
ambiente = Ambiente(robot, laberinto)

# Chequea que tenga salida el laberinto
print "El laberinto tiene salida?", ambiente.chequear_solucion()

width = len(ambiente.matriz)*32
height = len(ambiente.matriz[0])*32
begin_graphics(width=width, height=height, title="SimBot")

#~ ambiente.visualizar()
ambiente.visualizar_oscuridad()
robot.salir_del_laberinto(ambiente)

print ambiente.matriz

#chequeo que no camine por las paredes
for i in robot.historia_posiciones:
    if ambiente.matriz[tuple(i)] == 1:
        print "OOPS el robot paso por arriba de una pared en ", i

# Comprueba que la suma de los consumos de las acciones sea igual al estado de la bateria
consumo_bateria = \
      len([i for i,x in enumerate(robot.historia_acciones) if x == 'l'])*1 + \
      len([i for i,x in enumerate(robot.historia_acciones) if x == 'r'])*1 + \
      len([i for i,x in enumerate(robot.historia_acciones) if x == 's'])*1 + \
      len([i for i,x in enumerate(robot.historia_acciones) if x == 'f'])*2 + \
      len([i for i,x in enumerate(robot.historia_acciones) if x == 'x'])*4 

print "consumo bateria: ",consumo_bateria, "diferencia calculos: ",consumo_bateria - (carga_inicial - robot.bateria)

end_graphics()






    
