'''
Esta es una clase de laberinto
'''
import numpy as np

class Laberinto():

    def __init__(self, entrada, salida, tamano_x, tamano_y):

        self.entrada = entrada 
        self.salida = salida   
        self.tamano_x = tamano_x 
        self.tamano_y = tamano_y
        
    def hacer(self, complexity=.75, density=.75):

        size = ((self.tamano_x // 2) * 2 + 1, (self.tamano_y // 2) * 2 + 1)

        self.tamano_x, self.tamano_y = size
   
        complexity = int(complexity * (5 * (size[0] + size[1])))
        density    = int(density * ((size[0] // 2) * (size[1] // 2)))
            # Build actual maze
        Z = np.zeros(size, dtype=np.int)
    # Fill borders
        Z[0, :] = Z[-1, :] = 1
        Z[:, 0] = Z[:, -1] = 1
        # Make aisles
        for i in range(density):
            x, y = np.random.random_integers(0, size[1] // 2) * 2, np.random.random_integers(0, size[0] // 2) * 2
            Z[y, x] = 1
            for j in range(complexity):
                neighbours = []
                if x > 1:             neighbours.append((y, x - 2))
                if x < size[1] - 2:  neighbours.append((y, x + 2))
                if y > 1:             neighbours.append((y - 2, x))
                if y < size[0] - 2:  neighbours.append((y + 2, x))
                if len(neighbours):
                    y_,x_ = neighbours[np.random.random_integers(0, len(neighbours) - 1)]
                    if Z[y_, x_] == 0:
                        Z[y_, x_] = 1
                        Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                        x, y = x_, y_

        Z[self.entrada] = 2
        Z[self.salida] = 3
        
        return Z