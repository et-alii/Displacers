#!/usr/bin/env python3

"""Displacers Mathematical Model

This module performs the mathematical calculations used in the Displacers
software. The main function is `iterate`, which implements the entire
calculations required for the model to operate. The rest of the functions in
this module are helper functions for `iterate`, and as such, they are stored as
private functions and are not to be used in other modules. Please read the
`iterate` function's docstring for more information on arguments.
"""

import numpy as np

def __ss(a: np.ndarray, b: np.ndarray) -> float:
    """
    Returns the sum of cross products of two equal-lenght arrays `a` and `b`.
    """
    return (a*b).sum() - a.sum() * b.sum() / len(a)


def __submatrix(matrix: np.ndarray, cx: int, cy: int, r: int=1) -> np.ndarray:
    """
    Given an input `matrix`, returns a submatrix of size 2`r`+1 by 2`r`+1
    with center in (`cx`, `cy`). If it is not possible to form a submatrix from
    the given conditions (e.g. when `cx` and/or `cy` are close to the borders),
    a trimmed matrix is returned.
    """

    height, width = matrix.shape

    # Define borders for submatrix
    left_limit   = 0 if cy-r < 0 else cy-r
    right_limit  = width+1 if cy+r > width-1 else cy+r+1
    top_limit    = 0 if cx-r < 0 else cx-r
    bottom_limit = height+1 if cx+r > height-1 else cx+r+1

    return matrix[left_limit:right_limit, top_limit:bottom_limit]


def __matrix_angles(
    matrix: np.ndarray, hscale: float=1.0, vscale: float=1.0
    ) -> tuple[float]:
    """
    Performs a three-dimensional linear regression on an input `matrix`. In
    particular, it uses matrix horizontal indices scaled by `hscale` as values
    for x, vertical indices scaled by `hscale` as values for y, and matrix
    values scaled by `vscale` as values for z, setting z as the dependent
    variable and x, y as independent variables. It computes the slope of x
    against z, and the slope of y against z, and returns the inverse tangents of
    both slopes to obtain corresponding angles.
    """

    # Define variables for linear regression
    height, width = matrix.shape
    x = np.tile(np.arange(width), height) * hscale
    y = np.arange(height).repeat(width) * hscale
    z = matrix.reshape(height*width) * vscale

    # Perform linear regression to obtain slopes
    mx = __ss(x, z) / __ss(x, x)
    my = __ss(y, z) / __ss(y, y)

    # Transform slopes to angles
    return np.arctan(mx), np.arctan(my)


def __accelerations(
    xangle: float, yangle: float, g: float=9.80665, mu: float=0.0
    ) -> tuple[float]:
    """
    Given a three-dimensional inclination, return the acceleration (in x and y)
    produced by the force of gravity. If no custom gravity is specified, the
    function will use Earth's Standard Gravity. You can also set a coefficient
    of friction, which by default is 0.
    """

    # Remove negative signs from input angles, if any
    xangle = np.fabs(xangle)
    yangle = np.fabs(yangle)

    # Calculate accelerations
    ax = g * (np.sin(xangle) - mu * np.cos(xangle))
    ay = g * (np.sin(yangle) - mu * np.cos(yangle))

    return ax, ay


def __next_state(
    px: float, py: float, ax: float, ay: float, xangle: float, yangle: float,
    vx: float=0.0, vy: float=0.0, hscale: float=1.0, dt: float=1.0
    ) -> tuple[float]:
    """
    Returns the new position and velocity of the displacer in the x and y
    components given a previous state as well as the accelerations calculated
    with the `accelerations` function.
    """

    # The direction of movement is given by the opposite sign of the angle
    # This is only needed when acceleration is positive
    dx = -np.sign(xangle)
    dy = -np.sign(yangle)

    # New total velocity in the x component
    if ax >= 0:
        nvx = vx + ax * dx * dt
    else:
        if vx >= 0:
            nvx = max(0, vx + ax * dt)
        else:
            nvx = min(0, vx - ax * dt)

    # New total velocity in the y component
    if ay >= 0:
        nvy = vy + ay * dy * dt
    else:
        if vy >= 0:
            nvy = max(0, vy + ay * dt)
        else:
            nvy = min(0, vy - ay * dt)
    
    # Obtain horizontal component from the total speeds. Only the horizontal
    # component affects the position, but the total velocity will still be
    # stored
    nvxh = nvx * np.cos(np.fabs(xangle))
    nvyh = nvy * np.cos(np.fabs(yangle))

    # Compute new positions
    npx = px + nvxh * dt / hscale
    npy = py + nvyh * dt / hscale

    return npx, npy, nvx, nvy


def iterate(
    terrain: np.ndarray, px: float, py: float, vx: float=0.0, vy: float=0.0,
    hscale: float=1.0, vscale: float=1.0, gravity: float=9.80665, mu: float=0.0,
    radius: int=1, dt: float=1.0, iter: int=1, return_all: bool=False,
    warn: bool=True
    ) -> list[dict[str, float]] | dict[str, float]:
    """
    Main function of the displacer simulation. The only required arguments are:
    the `terrain` over which the displacer will move, and the coordinates (`px`
    and `py`) of the initial position of the displacer. By default, the function
    returns a list of dictionaries with the states on every iteration, unless
    the `return_all` parameter is set to `False`. The dictionaries produced by
    this functions contain four keys, `px`, `py`, `vx` and `vy`, corresponding
    to the location and speed of the displacer at any given moment.

    Arguments:
    - `terrain` (`np.ndarray`): 2D-array representing the heightmap of the
    location on which the displacer will move. Normally, it takes as parameter
    an image (transformed to an array) with each pixel having values between 0
    and 255, inclusive. If this is not taken into account, the function may
    return unexpected results (due, in particular, to floating point errors).
    - `px`, `py` (`float`): Initial coordinates (in pixels) of the displacer.
    - `vx`, `vy` (`float`, default = `0.0`): Initial velocities (in m/s) of the
    displacer.
    - `hscale`, `vscale` (`float`, default = `1.0`): Values (in meters) used to
    scale the terrain horizontally and vertically, or, in other words, `hscale`
    defines the number of meters each pixel in the original terrain represents,
    whereas `vscale` defines the number of meters of height that each pixel
    value represents.
    - `g` (`float`, default = `9.80665`): Value for gravitational acceleration
    (in m/s²). Defaults to Earth's Standard Gravity.
    - `mu` (`float`, default = `0.0`): Value for the coefficient of friction.
    Defaults to no friction.
    - `r` (`int`, default = `1`): "Radius" (in pixels) surrounding the displacer
    that will be taken into account to compute terrain inclination.
    - `dt` (`float`, default = `1.0`): Value for Δt (in seconds).
    - `n` (`int`, default = `1`): Number of iterations to perform.
    - `return_all` (`bool`, default = `False`): If set to `True`, the function
    returns a list of of every calculated state. Otherwise, and by default, it
    will only return the final state.
    - `warn` (`bool`, default = `True`): Whether to print a warning message if
    displacer is outside of terrain boundaries.
    """

    # Transform inputs to appropiate types
    px, py, vx, vy = float(px), float(py), float(vx), float(vy)
    hscale, vscale, gravity = float(hscale), float(vscale), float(gravity)
    mu, radius, dt, iter = float(mu), int(radius), float(dt), int(iter)

    # Initialize result list
    result = []
    result.append({"px": px, "py": py, "vx": vx, "vy": vy})
    height, width = terrain.shape

    # On each iteration
    for i in range(iter):

        # Get positions and velocities of the previous iteration
        px = result[-1]["px"]
        py = result[-1]["py"]
        vx = result[-1]["vx"]
        vy = result[-1]["vy"]

        # Check if displacer is inside the terrain, abort if True
        if px < 0 or px > width-1 or py < 0 or py > height-1:
            if warn == True:
                print(
                    f"WARNING: Stopped on iteration {i} because object is "
                    f"located outside of terrain boundaries."
                )
            break

        # Round positions to closest integer
        cx = int(round(px))
        cy = int(round(py))

        # Submatrix of radius r taken from the terrain
        mat = __submatrix(terrain, cx, cy, radius)

        # Inclination
        xangle, yangle = __matrix_angles(mat, hscale, vscale)

        # Accelerations
        ax, ay = __accelerations(xangle, yangle, gravity, mu)

        # Next state
        npx, npy, nvx, nvy = __next_state(
            px, py, ax, ay, xangle, yangle, vx, vy, hscale, dt
        )

        # Append the obtained state to the result list
        # print({"px": npx, "py": npy, "vx": nvx, "vy": nvy})
        result.append({"px": npx, "py": npy, "vx": nvx, "vy": nvy})

    # Return result
    if return_all == True:
        return result
    else:
        return result[-1]
