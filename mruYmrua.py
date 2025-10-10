from matplotlib.patches import FancyArrowPatch
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

import numpy as np


def generarGraficosMRU(cambiosAceleracion, vi):
    # cambiosAceleracion : dict en forma
    # cambiosAceleracion = {t1, aceleracion1}
    # vi : velocidad inicial
    # tf : tiempo total

    n = 0

    fig, ax = plt.subplots()

    ax.spines.top.set(visible=False)
    ax.spines.right.set(visible=False)

    ax.spines.bottom.set(position=('data', 0))
 
    for cambioAceleracion in cambiosAceleracion:
        n += 1
        ax.plot(0, 0,"o")
    
    

    fig.set_figwidth(7)

    plt.show()
    
#def graficaVT(cambiosAceleracion, vi, tf):


def graficaAT(cambiosAceleracion, mostrarAreas=False):
    n = 0
    fig, ax = plt.subplots()

    ax.spines.top.set(visible=False)
    ax.spines.right.set(visible=False)

    ax.spines.bottom.set(position=('data', 0))

    for tiempo in cambiosAceleracion:
        n += 1
        ti = float(tiempo.split('-')[0])
        tf = float(tiempo.split('-')[1])
        ax.hlines(cambiosAceleracion[tiempo], ti, tf)
        if mostrarAreas and cambiosAceleracion[tiempo] != 0:
            ax.annotate(r'$\Delta v_{0}$'.format(n), 
                        xy=(0,0), 
                        xycoords='data', 
                        xytext=(ti + (tf-ti)/2, cambiosAceleracion[tiempo]/2),
                        size=14,
                        horizontalalignment='center')
            ax.add_patch(Rectangle((ti, 0), tf-ti, cambiosAceleracion[tiempo], color='whitesmoke'))
            ax.vlines(ti, 0, cambiosAceleracion[tiempo], colors='gainsboro', ls='--')
            ax.vlines(tf, 0, cambiosAceleracion[tiempo], colors='gainsboro', ls='--')

    plt.show()

testing = {'0-5': 2, '5-10': -10, '10-12': 3}
#generarGraficosMRU(testing, 0, 6)

graficaAT(testing, True)