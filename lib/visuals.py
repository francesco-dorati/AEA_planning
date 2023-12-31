import matplotlib.pyplot as plt
import numpy as np
 

class Visuals:
    def __init__(self):
        plt.rcParams['figure.figsize'] = 12, 12
        self.layers = 0
        self.plt = plt

    def add_grid(self, grid):
        if self.layers == 0:
            plt.imshow(grid, cmap='Greys', origin='lower')
            self.layers += 1
        else:
            plt.imshow(grid, cmap='Greys', origin='lower', alpha=0.7)

    
    def add_point(self, point: tuple, color='x'):
        x, y = point
        plt.plot(y, x, color)
    
    def add_path(self, path, color='r'):
        pp = np.array(path)
        plt.plot(pp[:, 1], pp[:, 0], color)

    
    
    def show(self):
        plt.show()