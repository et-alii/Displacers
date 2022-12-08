#!/usr/bin/env python3

"""Displacers Animation Creator

This script provides the `create` function, with which the animations are
produced within the main software.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create(
    terrain: np.ndarray, states: list[dict[str, float]]) -> FuncAnimation:
    """
    Produces an animation object from a list of states created by the
    `model.iterate` function and an 2D-array representing the terrain.
    """

    # Create a figure with an image
    fig, ax = plt.subplots()
    height, width = terrain.shape
    plt.imshow(terrain, cmap="gray")
    plt.axis("off")
    x, y = None, None
    ln, = ax.plot([], [], 'ro')

    # Initialization function
    def init():
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
        return ln,

    # Update function for each state
    def update(frame):
        x = states[frame]["px"]
        y = states[frame]["py"]
        ln.set_data(x, y)
        return ln,

    # Output animation object
    return FuncAnimation(
        fig=fig, func=update, frames=np.arange(0, len(states)),
        init_func=init, blit=True, interval=50, repeat=True
    )