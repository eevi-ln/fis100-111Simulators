from matplotlib.patches import FancyArrowPatch
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon

import numpy as np


def generarGraficosMRUA(cambiosAceleracion, vi=0, mostrarAreas=False, unidadD='m', unidadT='s'):
    graficaVT(cambiosAceleracion, vi, mostrarAreas, unidadD, unidadT)
    graficaAT(cambiosAceleracion, mostrarAreas, unidadD, unidadT)
    
def graficaVT(cambiosAceleracion, vi=0, mostrarAreas=False, unidadD="m",unidadT="s"):
    n = 0
    fig, ax = plt.subplots()

    ax.set_ylabel(f"velocidad [{unidadD}/{unidadT}]")
    ax.set_xlabel(f"tiempo [{unidadT}]")
    ax.spines.top.set(visible=False)
    ax.spines.right.set(visible=False)

    ax.spines.bottom.set(position=('data', 0))

    xdata=[]
    ydata=[]

    vf = vi
    ydata.append(vi)

    for tiempo in cambiosAceleracion:
        n+= 1
        #print(n)
        ti = float(tiempo.split('-')[0])
        tf = float(tiempo.split('-')[1])

        dv = (tf - ti) * cambiosAceleracion[tiempo]

        vf += dv

        if ti not in xdata: xdata.append(ti)
        xdata.append(tf)
        ydata.append(vf)

        if(ydata[n-1] > 0 and ydata[n] < 0) or (ydata[n-1] < 0 and ydata[n] > 0):
            print(n-1)
            print(n)
            xdata.insert(n, abs(ydata[n-1]/cambiosAceleracion[tiempo]) + ti)
            print(ydata[n-1]/cambiosAceleracion[tiempo])
            ydata.insert(n, 0)
            n+=1
        
    i = 1
    while i < len(xdata):
        if mostrarAreas and not (ydata[i-1] == 0 and ydata[i] == 0):
            ax.annotate(r'$\Delta x_{0}$'.format(i), 
                        xy=(0,0), 
                        xycoords='data', 
                        xytext=(xdata[i-1] + (xdata[i]-xdata[i-1])/2, 0),
                        size=14,
                        horizontalalignment='center',
                        verticalalignment='bottom')
            ax.add_patch(Polygon(((xdata[i-1], ydata[i-1]),
                                 (xdata[i-1], 0),
                                 (xdata[i], 0),
                                 (xdata[i], ydata[i])), 
                                 color='whitesmoke'))
            ax.vlines(xdata[i-1], 0, ydata[n-1], colors='gainsboro', ls='--')
            ax.vlines(xdata[i], 0, ydata[i], colors='gainsboro', ls='--')
        i+=1

        
    print(xdata)
    print(ydata)
    ax.plot(xdata, ydata, color='xkcd:cobalt blue')

    fig.savefig("mruaVT.png")
    #plt.show()

def graficaAT(cambiosAceleracion, mostrarAreas=False, unidadD="m", unidadT="s"):
    n = 0
    fig, ax = plt.subplots()

    
    ax.set_ylabel(r"aceleración [{0}/${1}^2$]".format(unidadD, unidadT))
    ax.set_xlabel(f"tiempo [{unidadT}]")
    ax.spines.top.set(visible=False)
    ax.spines.right.set(visible=False)

    ax.spines.bottom.set(position=('data', 0))

    for tiempo in cambiosAceleracion:
        n += 1
        ti = float(tiempo.split('-')[0])
        tf = float(tiempo.split('-')[1])
        ax.hlines(cambiosAceleracion[tiempo], ti, tf, color='xkcd:scarlet')
        if mostrarAreas and cambiosAceleracion[tiempo] != 0:
            ax.annotate(r'$\Delta v_{0}$'.format(n), 
                        xy=(0,0), 
                        xycoords='data', 
                        xytext=(ti + (tf-ti)/2, cambiosAceleracion[tiempo]/2),
                        size=14,
                        horizontalalignment='center',
                        verticalalignment='center')
            ax.add_patch(Rectangle((ti, 0), tf-ti, cambiosAceleracion[tiempo], color='whitesmoke'))
            ax.vlines(ti, 0, cambiosAceleracion[tiempo], colors='gainsboro', ls='--')
            ax.vlines(tf, 0, cambiosAceleracion[tiempo], colors='gainsboro', ls='--')

    fig.savefig("mruaAT.png")
    #plt.show()


testing = {'0-5': 1, '5-7': 0, '7-10': -3}
generarGraficosMRUA(testing, mostrarAreas=True)

graficaVT(testing, mostrarAreas=True)
#graficaAT(testing, True)