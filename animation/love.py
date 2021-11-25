import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 15)

    return ln,

def update(frame):

    xdata.append(np.sin(frame) ** 3 * 15)
    ydata.append(13 * np.cos(frame) - 5 * np.cos(2 * frame) - 2 * np.cos(3 * frame) - np.cos(4 * frame))
    ln.set_data(xdata, ydata)

    return ln,

writer = animation.PillowWriter(fps=24)
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 1000),
                    init_func=init, blit=True, repeat=True, interval=1)
ani.save("images/love.gif", writer=writer)
# plt.show()