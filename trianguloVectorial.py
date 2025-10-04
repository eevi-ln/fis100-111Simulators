import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow
import math

def disc(a, b, c): return b**2 - (4*a*c)

fig, ax = plt.subplots(nrows=2)

dx = 0      # desplazamiento eje x
dy = 0      # desplazamiento eje y

vi = 0      # magnitud velocidad inicial
angv = 0    # angulo velocidad inicial en deg
            # recordar funciones trigonométricas en rad en math.py
vxi = 0
vyi = 0

vf = 0
vxf = 0
vyf = 0

grav = 10   # gravedad redondeada
dt = 0      # delta tiempo

# notemos en ejercicios de este tipo realmente lo que importa son:
# velocidad inicial; su magnitud y ángulo y dy, en base a estos se calcula lo demás.

vinicial = 15
angulov = 50




desplazamiento = FancyArrow(0,0, dx, dy,width=0.3, color='k')

ax[0].add_patch(desplazamiento)
ax[0].set(xlim=(0,dx+5),ylim=(-15,0))

plt.show()