import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

# zu betrachtendes Gebiet // Größe = [ANFANG, ENDE]
t_gebiet = [-9, 9]
x_gebiet = [-5, 5]
# Anzahl der Pfeile auf jeder Achse
N = 30

def f(x,t):
    f = x**3 - t
    return f

t = np.linspace(t_gebiet[0], t_gebiet[1], N)
x = np.linspace(x_gebiet[0], t_gebiet[1], N)
[T,X] = np.meshgrid(t,x)

#Werte für 2-D Graph
F = f(X,T)

#Vekorkomponenten
Vt = 1/np.sqrt(1+ F**2)
Vx = Vt*F
norm = np.sqrt(1+F**2)

#Plotten
fig, axes = plt.subplots()
axes.set_aspect('equal')
axes.quiver(T,X,Vt,Vx,norm, cmap='plasma')
CS = axes.contour(T,X,F,levels=10, cmap='seismic') #isoklinen
axes.clabel(CS, inline=1, fontsize=10)
axes.tick_params(bottom=True, left=True, right=True, top=True, direction='in')
axes.set_xlabel('t')
axes.set_ylabel('x')
plt.show()