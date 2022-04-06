#importing the required module

#pip install matplotlib==3.0.3

import matplotlib.pyplot as plt

#x axis values
x = [1,2,3]

#corresponding y axis values
y = [2,4,1]

# plotting the points
plt.plot(x,y)

#naming the x axis
plt.xlabel('x - axis')

#nameing the y axis
plt.ylabel('y - axis')

#giving a title to my graphe
plt.title('My first graph')

#function to show the plot
plt.show()

