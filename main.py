import numpy as np
from gasp import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation

import argparse

from source.ambiente import Ambiente
from source.robot import Robot
from source.grafico import Grafico
from source.laberintos.deep_first_search import Laberinto

from source.estrategias.hamster import Hamster
from source.estrategias.buscador_por_derecha import Buscador_por_derecha
from source.estrategias.perseo import Perseo


parser = argparse.ArgumentParser()
parser.add_argument("-g", "--grafico",action="store_true", help="Muestra el laberinto", default=False)
args = parser.parse_args()

def main():
    tamano_x, tamano_y = (100, 100)
    entrada = (1,1)
    salida = (tamano_x-2,tamano_y-2)

    pos_robot = np.array(entrada)
    ori_robot = np.array((0,1))

    hamster = Hamster()
    perseo = Perseo()
    buscador_por_derecha = Buscador_por_derecha()

    carga_inicial = 0

    robot = Robot(ori_robot, pos_robot, hamster, carga_inicial)

    laberinto = Laberinto(entrada, salida, tamano_x, tamano_y)
    ambiente = Ambiente(robot, laberinto)
    
    if args.grafico:
        grafico = Grafico(1,ambiente.matriz, laberinto.entrada, laberinto.salida)
    width = len(ambiente.matriz)*32
    height = len(ambiente.matriz[0])*32
    
    if args.grafico:
        begin_graphics(width=width, height=height, title="SimBot")
        grafico.visualizar()

    #plt.imshow(ambiente.matriz, cmap=plt.cm.gray, interpolation='nearest')
    #plt.show()    
        
    robot.salir_del_laberinto(ambiente)
    '''
    def init():
        #Draw background
        plt.imshow(ambiente.matriz, interpolation="none", hold=True)
    
    def hacer_ani(pos):
        ambiente.matriz[tuple(pos)] = 8
        return ambiente.matriz

    fig = plt.figure(figsize=(20,20))
    ani = animation.FuncAnimation(fig, hacer_ani, robot.historia_posiciones, init_func=init, frames=200, interval=10, blit=True,repeat=False)
    ani.save('ps.mp4', writer=writer)
    plt.show()
    '''
    '''
    fig = plt.figure()

    myimages = []
    
    for p in robot.historia_posiciones:
        imgplot = ambiente.matriz[tuple(p)] = 8
        myimages.append([imgplot])

    my_anim = animation.ArtistAnimation(fig, myimages, interval=1000, blit=True, repeat_delay=1000)
    '''
    #plt.show()
if __name__ == "__main__":
    main()
