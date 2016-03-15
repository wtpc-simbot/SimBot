
import numpy as np
from ambiente import Ambiente
from robot import Robot

tamano_x, tamano_y = (10,10)
entrada = (1,1)
salida = (tamano_x-2,tamano_y-2)
pos_robot = np.array(entrada)
ori_robot = np.array((0,1))
robots = Robot(pos_robot,ori_robot)



for cual_ambiente in xrange(4):
    ambiente = Ambiente(entrada,salida,tamano_x,tamano_y,robots,cual_ambiente)
    print ambiente.matriz
    print "tiene solucion?" , ambiente.chequear_solucion()
    print "distancia: ", ambiente.sensar()





