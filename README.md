# Displacers

National Autonomous University of Mexico (https://www.unam.mx/).

- Maria Lucrecia Beltz Gonzalez ([Lucreciabeltz](https://github.com/Lucreciabeltz))
- Karime Ochoa Jacinto ([Kadkam8a](https://github.com/Kadkam8a))
- Debora Joselyn Tolentino Diaz ([Debytd](https://github.com/Debytd))
- Anton Pashkov ([aapashkov](https://github.com/aapashkov))

## License

Copyright © 2022 <pashkov@comunidad.unam.mx, karime8aj@gmail.com, deborajtd.12@gmail.com, lucreciabeltz@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Introduction


This project consists of a mathematical model of the movement of a sphere on an irregular surface in order to output a graphical, bidimensional visualization of how its trajectory would look from a given point.

For it, the main function requires from the user two basic parameters:
- The terrain over which the displacer will move. 
- The coordinates (px, py) of the initial position of the displacer.

Other specifications as the initial speed, gravitational acceleration value, coefficient of friction, etc. can optionally be modified by the user. 

The obtained visualization will show the user the sphere movements in the axis x, and y by left-right and up-down movements, and the movements over the z-axis will be represented by the color of the pixel in the provided image where a value of 0 will represent the lowest point in the terrain and the value 255 the highest.  

<img src=https://github.com/et-alii/Displacers/blob/main/examples/irregular.png>

## Objetives

- Generate a model of the movement of a sphere on an irregular surface.
- Create a graphical visualization of the model from the provided parameters.
## Metodology
### Mathematical Formulas
For the calculations two formulas were required.

#### Acceleration function
We know that the formula to calculate acceleration is $a = F/m$, however, by having the object on an inclined surface, its weight is divided into 2 forces: one on the $X$ axis and another on the $Y$ axis.
The angle of inclination of the surface is the same angle formed between the force in the $Y$ axis and the weight of the object, therefore if we move the vector of the force in $X$ in a parallel way, we will have the necessary trigonometry to obtain the forces:
![Image](https://user-images.githubusercontent.com/60940990/206359851-b574ad10-6b31-4708-b05f-0421e5084f1c.gif)
$Fx = P * sin𝛳$

$Fy = P * cos𝛳$, if we substitute the weight for: $P = m * g$: 
$Fx = m * g * sin𝛳$ y  $Fy = m * g * cos𝛳$

In addition to the previous decomposition there is a force that arises from $Fy$ that exists due to friction with the surface, called friction force $(Ff)$. The movement will depend on this force, because if $Ff$ is greater than the angle of inclination of the surface $(𝛳)$, the object will remain at rest; likewise, if $Ff$ is less than $𝛳$, then the body will descend with a uniformly accelerated motion.

The maximum value that $Ff$ can have is given by $μ = Ff/Fy$, where solving for $Ff$ we have that $Ff = μ * Fy = μ * m * g * cos𝛳$, therefore, if we want there to be movement we look for $Fx = Ff$ .

Substituting $Fx$ and $Ff$ we have:

$m * g * sin𝛳 = μ * m * g * cos𝛳$, simplifying the equation:

$sin𝛳 = μ * cos𝛳$.

The trig ratio relating $sin𝛳$ and $cos𝛳$ is $tan𝛳$, therefore:

$μ = tan𝛳$ and $𝛳 = arctan μ$

The resultant force of the two forces acting on the object is:

$FR = m * g * sin𝛳 – μ * m * g * cos𝛳 = m * g * (sin𝛳 – μ * cos𝛳)$

Finally, the fundamental principle of dynamics is applied: 

$a = F/m$

$a = m * g * (sin𝛳 – μ * cos𝛳) / m$

Simplify and we have:

$a = g * (sin𝛳 – μ * cos𝛳)$

#### Matrix angles

Performs a three-dimensional linear regression on a matrix, it uses matrix horizontal indices scaled by $hscale$ as values for $x$, vertical indices scaled by $hscale$ as values for $y$ and matrix values scaled by $vscale$ as values for $z$, setting $z$  as the dependent variable and $x, y$ as independent variables.  It computes the slope of $x$ against $z$ and the slope of $y$ against $z$, and returns the inverse tangents of both slopes to obtain corresponding angles.

The values $hscale$ and $vscale$ represent the appropriate scale for the entered terrain.

In order to obtain the angles the next formula was applied in the linear regression.

$\theta = \arctan \frac{\Sigma i d - (\Sigma i \Sigma d) \div n}{\Sigma i i  -  (\Sigma i \Sigma i)\div n}$ 

Where $i$ is the independent variable and $d$ the dependent one. 




## Objectives

