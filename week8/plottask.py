# plottask.py
# This program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

# Author: Roberto Vergano

#Line 7 and 8 to import the modules numpy and marplotlib
import numpy as np
import matplotlib.pyplot as plt

#Line 11 creates an array of numbers in the range 0 to 4.
x = np.array(range(0,4))
#Line 13 and 14 defines the variables "g" and "h" for the functions g(x) and h(x)
g = x*x
h = x*x*x

#The following lines customize the plot.
plt.plot(x,label = "f(x)",linestyle= "dashed",linewidth= 4)
plt.plot(g,label = "g(x)", linestyle= ":", linewidth = 4)
plt.plot(h,label = "h(x)", linestyle= "-.", linewidth = 4)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Plottask")
plt.legend() 
plt.show()
