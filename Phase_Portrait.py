import numpy as np
import matplotlib.pyplot as plt

#intervall
x_gebiet = np.arange(-1,2.5,0.01)
y_gebiet = np.arange(-1.5,1.5,0.01)
[X,Y]= np.meshgrid(x_gebiet,y_gebiet)

#system ('**' = '^')
xdot = Y
ydot = X + 0.1*Y-X**2

#colorizing
speed = np.sqrt(xdot**2+ydot**2)

#plot
fig, axes=plt.subplots()
axes.streamplot(X,Y,xdot,ydot, color=speed, cmap='plasma', density=1.5)
axes.set_aspect('equal')
axes.set_xlabel('x')
axes.set_ylabel(r'$\partial_t x$')
axes.tick_params(left=True,bottom=True,top=True,right=True, direction='in')
axes.grid(True, alpha=0.5)
plt.show()