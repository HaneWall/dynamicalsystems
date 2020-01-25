import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#intervall
x_gebiet = np.arange(-1,2.5,0.01)
y_gebiet = np.arange(-1.5,1.5,0.01)
[X,Y]= np.meshgrid(x_gebiet,y_gebiet)

#plot
fig, axes=plt.subplots()
axes.set_aspect('equal')
axes.set_xlabel('x')
axes.set_ylabel(r'$\partial_t x$')
axes.tick_params(left=True,bottom=True,top=True,right=True, direction='in')
axes.grid(True, alpha=0.5)
axes.set_ylim([-1.5,1.5])
axes.set_xlim([-1,2.5])

#system
xdot = Y
ydot = X - 3 * Y - X ** 2
speed = np.sqrt(xdot**2+ydot**2)
stream = axes.streamplot(X,Y,xdot,ydot, color=speed, cmap='plasma', density=1.5)

def update(i):
    axes.collections = []  # clear lines streamplot
    axes.patches = []  # clear arrowheads streamplot
    xdot = Y
    ydot = X - (3-0.06*i) * Y - X ** 2
    speed = np.sqrt(xdot**2+ydot**2)
    mu = -(3-0.06*i)
    axes.set_title(r'$\mu$ = %f' %mu)
    stream = axes.streamplot(X,Y,xdot,ydot, color=speed, cmap='plasma', density=1.5)
    print(i)
    return stream

anim = animation.FuncAnimation(fig, update, frames=100, interval=100, blit=False, repeat=False)
plt.show()
#anim.save('./animation.gif', writer='imagemagick', fps=8)
