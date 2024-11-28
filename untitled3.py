# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TCvrZL3Vcxf6ZIjqjTxd1ImagfwN9-Sy
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Set up the figure and the axis
fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)

# Initialize an empty line object
line, = ax.plot([], [], lw=2)

# Initialize the data
x = np.linspace(0, 2 * np.pi, 100)

# Initialization function to plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# Animation function which updates the plot
def animate(i):
    y = np.sin(x + i / 10.0)
    line.set_data(x, y)
    return line,

# Create the animation
ani = FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

# Display the animation in the notebook
HTML(ani.to_jshtml())