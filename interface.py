#!/usr/bin/env python3

"""Displacers Command Line Interface

This module parses command line arguments entered by the user and provides a
simple command line interface with help messages. The main function is 
`read`, which should take as parameter the `sys.argv` list and returns two
dictionaries: one with the parameters that must be loaded into `model.iterate`,
and a second one with additional parameters regarding the output that the user
requires. The first dictionary can be loaded easily into `model.iterate` by
typing something like `model.iterate(**dictionary)`. The second dictionary
includes three items:

- `output` (`None` or `str`): Name of the output GIF file. If None it means the
user didn't type the `--output` parameter.
- `html` (`False` or `True`): Returns whether the user typed the `--html` flag
or not.
- `rminput` (`False` or `True`): Returns whether the user asked to delete the
input image or not.

This module also provides the progress function, which is used to show a
progress bar when saving the output to a GIF and when the user has set the
--warn argument in his command.
"""

import sys
import argparse

import matplotlib.image as image


def read(input_arguments: list[str]) -> tuple[dict]:
    """Parses command line arguments."""

    arguments = [
        "--terrain", "--px", "--py", "--vx", "--vy", "--hscale", "--vscale",
        "--gravity", "--mu", "--radius", "--dt", "--iter", "--warn", "--output",
        "--html", "--rminput"
    ]

    argument_config = [
        {"required": True, "help": "png image with elevation data"}, # terrain
        {"required": True, "type": float, "help": (                  # px
            "initial x coordinate in pixels of the displacer")},
        {"required": True, "type": float, "help": (                  # py
            "initial y coordinate in pixels of the displacer")},
        {"type": float, "default": 0.0, "help": (                    # vx
            "(default = 0.0) initial speed in the x component in m/s")},
        {"type": float, "default": 0.0, "help": (                    # vy
            "(default = 0.0) initial speed in the y component in m/s")},
        {"type": float, "default": 1.0, "help": (                    # hscale
            "(default = 1.0) meters per pixel scale")},
        {"type": float, "default": 1.0, "help": (                    # vscale
            "(default = 1.0) meters per pixel color scale")},
        {"type": float, "default": 9.80665, "help": (                # gravity
            "(default 9.81) acceleration of gravity in m/s²")},
        {"type": float, "default": 0.0, "help": (                    # mu
            "(default 0.0) coefficient of friction")},
        {"type": int, "default": 1, "help": (                        # radius
            "(default 1) radius in pixels surrounding the displacer used to "
            "compute the inclination of the terrain below its location")},
        {"type": float, "default": 1.0, "help": (                    # dt
            "(default 1.0) value for Δt in seconds")},
        {"type": int, "default": 200, "help": (                      # iter
            "(default 200) number of iterations")},
        {"default": False, "action": "store_true", "help": (         # warn
            "(default not written) if used, show warning messages if any")},
        {"default": None, "help": (                                  # output
            "(default not written) output gif file")},
        {"default": False, "action": "store_true", "help": (         # html
            "(default not written) whether to write html to standard output")},
        {"default": False, "action": "store_true", "help": (         # rminput
            "(default not written) whether to delete input image at the end")}
    ]

    parser = argparse.ArgumentParser(
        prog=input_arguments[0],
        description=(
            "Simulate the movement of an object (a displacer) over an "
            "irregular terrain surface.\n\n"
            "Visit https://github.com/et-alii/Displacers to view the full "
            "documentation, license, and source code of this software."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    for argument, config in zip(arguments, argument_config):
        parser.add_argument(argument, **config)

    # Show help message if no arguments were given
    if len(input_arguments) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Parse arguments
    model_config = vars(parser.parse_args(input_arguments[1:]))

    # Load image
    img = (image.imread(model_config["terrain"], "png") * 255)[:, :, :3]
    img = img.mean(axis=2)
    model_config["terrain"] = img

    # Split dictionaries
    output_config = {}
    for key in ["output", "html", "rminput"]:
        output_config[key] = model_config.pop(key)

    return model_config, output_config


def progress(current, total):
    """
    Prints a progress bar in standard output while animation is being saved to
    GIF. Only shown if there is a --warn argument in the shell command.
    """
    print(f"\rProgress: {current/total*100:.2f}%", end="")
