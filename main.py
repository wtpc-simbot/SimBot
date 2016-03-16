
import numpy as np
from gasp import *
from source.ambiente import Ambiente
from source.robot import Robot

from source.estrategias.hamster import Hamster

tamano_x, tamano_y = (15,15)
entrada = (1,1)
salida = (tamano_x-2,tamano_y-2)
pos_robot = np.array(entrada)
ori_robot = np.array((0,1))

hamster = Hamster()
carga_inicial = 1000000

robot = Robot(ori_robot, pos_robot, hamster, carga_inicial)

cual_ambiente = 2

ambiente = Ambiente(entrada, salida, tamano_x, tamano_y, robot, cual_ambiente)

print "El laberinto tiene salida?", ambiente.chequear_solucion()

robot.salir_del_laberinto(ambiente)

print ambiente.matriz


#chequeo que no camine por las paredes
for i in robot.historia_posiciones:
    if ambiente.matriz[tuple(i)] == 1:
        print "OOPS el robot paso por arriba de una pared en ", i

consumo_bateria = \
      len([i for i,x in enumerate(robot.historia_acciones) if x == 'l'])*1 + \
      len([i for i,x in enumerate(robot.historia_acciones) if x == 'r'])*1 + \
      len([i for i,x in enumerate(robot.historia_acciones) if x == 's'])*1 + \
      len([i for i,x in enumerate(robot.historia_acciones) if x == 'f'])*2 + \
      len([i for i,x in enumerate(robot.historia_acciones) if x == 'x'])*4 

print "consumo bateria: ",consumo_bateria, "diferencia calculos: ",consumo_bateria - (carga_inicial - robot.bateria)


'''
for cual_ambiente in xrange(4):
    ambiente = Ambiente(entrada,salida,tamano_x,tamano_y,robots,cual_ambiente)
    print ambiente.matriz
    print "tiene solucion?" , ambiente.chequear_solucion()
    print "distancia: ", ambiente.sensar()

PARA GRAFICAR

width = len(laberinto.matriz)*32
height = len(laberinto.matriz[0])*32
begin_graphics(width=width, height=height, title="SimBot")
una_prueba.visualizar()
una_prueba.actualizar([0,0],[0,1])
una_prueba.actualizar([0,1],[0,2])
una_prueba.actualizar([0,2],[0,3])
una_prueba.actualizar([0,3],[1,3])
end_graphics()
    
 '''






    