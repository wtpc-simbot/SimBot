import numpy as np
from gasp import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation

from source.ambiente import Ambiente
from source.robot import Robot
from source.grafico import Grafico
from source.laberintos.deep_first_search import Laberinto

from source.estrategias.hamster import Hamster
from source.estrategias.buscador_por_derecha import Buscador_por_derecha

def main():
    tamano_x, tamano_y = (10,10)
    entrada = (1,1)
    salida = (tamano_x-2,tamano_y-2)
    salida = (tamano_x-1,tamano_y-1)


    pos_robot = np.array(entrada)
    ori_robot = np.array((0,1))

    hamster = Hamster()
    buscador_por_derecha = Buscador_por_derecha()

    carga_inicial = 0

    robot = Robot(ori_robot, pos_robot, hamster, carga_inicial)

    laberinto = Laberinto(entrada, salida, tamano_x, tamano_y)
    ambiente = Ambiente(robot, laberinto)
    #grafico = Grafico(0.5,ambiente.matriz, laberinto.entrada, laberinto.salida)

    width = len(ambiente.matriz)*32
    height = len(ambiente.matriz[0])*32
    #begin_graphics(width=width, height=height, title="SimBot")

    #grafico.visualizar()

    robot.salir_del_laberinto(ambiente)
    
    #end_graphics()


if __name__ == "__main__":
    main()
