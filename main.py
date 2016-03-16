
import numpy as np
from gasp import *
from source.ambiente import Ambiente
from source.robot import Robot
import time
from source.estrategias.hamster import Hamster

tamano_x, tamano_y = (10,10)
entrada = (1,1)
salida = (tamano_x-2,tamano_y-2)
pos_robot = np.array(entrada)
ori_robot = np.array((0,1))

hamster = Hamster()
robot = Robot(ori_robot, pos_robot, hamster)
cual_ambiente = 1

ambiente = Ambiente(entrada, salida, tamano_x, tamano_y, robot, cual_ambiente)

width = len(ambiente.matriz)*32
height = len(ambiente.matriz[0])*32
begin_graphics(width=width, height=height, title="SimBot")

ambiente.visualizar()
robot.salir_del_laberinto(ambiente)

end_graphics()
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






    
