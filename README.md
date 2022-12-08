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


# Acceleration function
We know that the formula to calculate acceleration is a = F/m , however, by having the object on an inclined surface, its weight is divided into 2 forces: one on the X axis and another on the Y axis.
The angle of inclination of the surface is the same angle formed between the force in the Y axis and the weight of the object, therefore if we move the vector of the force in X in a parallel way, we will have the necessary trigonometry to obtain the forces:
![Image](https://user-images.githubusercontent.com/60940990/206359851-b574ad10-6b31-4708-b05f-0421e5084f1c.gif)Fx = P * sen 𝛳 
Fy = P * cos 𝛳, if we substitute the weight for: P = m * g: Fx = m * g * sen 𝛳 y  Fy = m * g * cos 𝛳

In addition to the previous decomposition there is a force that arises from Fy that exists due to friction with the surface, called friction force (Ff). The movement will depend on this force, because if Ff is greater than the angle of inclination of the surface (𝛳), the object will remain at rest; likewise, if Ff is less than 𝛳, then the body will descend with a uniformly accelerated motion.

The maximum value that Ff can have is given by μt = Ff/Fy, where solving for Ff we have that Ff = μt * Fy = μt * m * g * cos 𝛳, therefore, if we want there to be movement we look for Fx = Ff .

Substituting Fx and Ff we have:
m * g * sin 𝛳 = μt * m * g * cos 𝛳, simplifying the equation: sin 𝛳 = μt * cos 𝛳.

The trig ratio relating sin 𝛳 and cos 𝛳 is tan 𝛳, therefore:
μt = tan 𝛳 and 𝛳 = arctan μt

The resultant force of the two forces acting on the object is:
FR = m * g * sin 𝛳 – μt * m * g * cos 𝛳 = m * g * (sin 𝛳 – μt * cos 𝛳)

Finally, the fundamental principle of dynamics is applied: 
a = F/m
a = m * g * (sin 𝛳 – μt * cos 𝛳) / m
Simplify and we have:
a = g * (sin 𝛳 – μt * cos 𝛳)




## Hypothesis



## Objectives

