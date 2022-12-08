#!/usr/bin/env python3

"""Displacers Main Software

Script to be executed by the user. One can use ./main.py --help to get all
available parameters to adjust.
"""

import sys

import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

import model
import interface
import animator

if __name__ == "__main__":

    # Parse CLI arguments into dictionaries
    model_config, output_config = interface.read(sys.argv)

    # Run simulation
    simulation = model.iterate(**model_config, return_all=True)

    # Create animation
    animation = animator.create(model_config["terrain"], simulation)

    # Output animation as asked by user
    if output_config["output"] == None:
        if output_config["html"] == True:
            print(animation.to_html5_video())
        else: plt.show()
    else:
        progress = interface.progress if model_config["warn"] == True else None
        animation.save(
            output_config["output"], writer=FFMpegWriter(fps=30), 
            progress_callback=progress)
        print("\rFinished!        ")
        if output_config["html"] == True:
            print(animation.to_html5_video())