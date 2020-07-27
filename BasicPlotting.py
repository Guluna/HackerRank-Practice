import matplotlib.pyplot as plt

myLinear = []
myQuadratic = []
myExponential = []

for i in range(30):
    myLinear.append(i)
    myQuadratic.append(i**2)
    myExponential.append(1.5**i)
    
plt.figure('Quadratic function')    # plots in a separate window & can be referred to easily later anywhere in the code
plt.plot(myLinear, myQuadratic)
plt.xlabel('X-Axis values')
plt.ylabel('Y-Axis values')
plt.title('Title of plot goes here')


plt.figure('Exponential function')
plt.title('First Expo fn')
plt.plot(myLinear, myExponential)


# comparing growth of quadratic & exponential fn by setting ylimit of both = 900
plt.figure('Quadratic function')    
plt.clf()   # clears all previous formatting associated with figure named ('Quadratic function')
plt.plot(myLinear, myQuadratic, 'b^', label = 'Quadratic', linewidth = 2.0)
plt.plot(myLinear, myExponential, 'ro', label = 'Exponential')
plt.title('Comparing growth of Quadratic & Expo fn in same window')
plt.ylim(0, 900)  # explicitly setting limits on y-axis
plt.legend(loc ='upper left')  # must define labels for legend 1st in plt.plot


# subplots
plt.figure('Quadratic function')    
plt.clf()  
plt.subplot(211)    # 2 rows 1 col & position of this plot in the whole frame
plt.title('Subplots')
plt.plot(myLinear, myQuadratic, 'b^', label = 'Quadratic', linewidth = 2.0)
plt.legend(loc ='upper left')
plt.subplot(212)
plt.plot(myLinear, myExponential, 'ro', label = 'Exponential')
plt.ylim(0, 900)
plt.legend(loc ='upper left')


# log scale
plt.figure('Quadratic function')    
plt.clf() 
plt.plot(myLinear, myQuadratic, 'b^', label = 'Quadratic', linewidth = 2.0)
plt.plot(myLinear, myExponential, 'ro', label = 'Exponential')
plt.title('Log scale on Y-axis')
plt.yscale('log')   # in log scale notice that exponential becomes linear 
plt.legend(loc ='upper left') 



