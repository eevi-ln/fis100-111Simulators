from matplotlib.patches import FancyArrowPatch
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

import numpy as np

"""
def generarGraficosMRU(cambiosAceleracion, vi, tf):
    # cambiosAceleracion : dict en forma
    # cambiosAceleracion = {t1, aceleracion1}
    # vi : velocidad inicial
    # tf : tiempo total

    fig, ax = plt.subplots()
 
    for cambioAceleracion in cambiosAceleracion:
        ax.plot(, 0,"o")
    
    

    fig.set_figwidth(7)

    plt.show()
"""
    
#def graficaVT(cambiosAceleracion, vi, tf):


def graficaAT(cambiosAceleracion):

    fig, ax = plt.subplots()

    ax.spines.top.set(visible=False)
    ax.spines.right.set(visible=False)

    ax.spines.bottom.set(position=('data', 0))

    for tiempo in cambiosAceleracion:
        t1, t2 = tiempo.split('-')
        ax.hlines(cambiosAceleracion[tiempo], t1, t2)
        
    plt.show()

testing = {'0-5': 2, '5-10': 0}
#generarGraficosMRU(testing, 0, 6)

graficaAT(testing)