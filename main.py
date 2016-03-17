import numpy as np
from gasp import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
import matplotlib.animation

from source.ambiente import Ambiente
from source.robot import Robot
from source.grafico import Grafico
from source.laberintos.deep_first_search import Laberinto

from source.estrategias.hamster import Hamster
from source.estrategias.buscador_por_derecha import Buscador_por_derecha


tamano_x, tamano_y = (13,13)
entrada = (1,1)
salida = (tamano_x-2,tamano_y-2)

pos_robot = np.array(entrada)
ori_robot = np.array((0,1))

hamster = Hamster()
buscador_por_derecha = Buscador_por_derecha()

carga_inicial = 0

robot = Robot(ori_robot, pos_robot, hamster, carga_inicial)
#~ robot = Robot(ori_robot, pos_robot, buscador_por_derecha, carga_inicial)

laberinto = Laberinto(entrada, salida, tamano_x, tamano_y)
ambiente = Ambiente(robot, laberinto)
grafico = Grafico(0.5,ambiente.matriz, laberinto.entrada, laberinto.salida)



# Chequea que tenga salida el laberinto
# print "El laberinto tiene salida?", ambiente.chequear_solucion()

width = len(ambiente.matriz)*32
height = len(ambiente.matriz[0])*32
begin_graphics(width=width, height=height, title="SimBot", background=color.BLACK)

#~ Funcion que inicializa el laberinto a oscuras
#~ grafico.visualizar_oscuridad()

grafico.visualizar()
posicion_sin_avanzar=robot.posicion.copy()
giro = robot.giroscopo.copy()
while not ambiente.estoy_fuera(): 
    posicion_sensada=robot.posicion + robot.giroscopo
    robot.mi_estrategia.decidir(robot, ambiente)
    grafico.visualizar_mirada(posicion_sin_avanzar, posicion_sensada,robot.giroscopo)
    grafico.actualizar(posicion_sin_avanzar, robot.posicion, robot.giroscopo)
    posicion_sin_avanzar=robot.posicion.copy()
    giro = robot.giroscopo.copy()
print ambiente.matriz

#chequeo que no camine por las paredes
for i in robot.historia_posiciones:
    if ambiente.matriz[tuple(i)] == 1:
        print "OOPS el robot paso por arriba de una pared en ", i


end_graphics()



fig = plt.figure(figsize= (5,5))
ax = fig.add_subplot(111)
cont = 0
for i in robot.historia_posiciones:
    i=robot.historia_posiciones[cont]
    mat=ambiente.matriz.copy()
    mat[i[0],i[1]] = 4
    ax.imshow(mat)
    fig.show()
    time.sleep(.1)
    cont += 1
    if cont>10:
        break

    
    
    
