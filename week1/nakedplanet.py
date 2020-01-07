###############################################################
# First Python script for the cousera course:                 #
# Global Warming II: Create Your Own Models in Python         #
# by: Bjoern Gam											  #
###############################################################

import matplotlib.pyplot as plt #for plotting the graph

###############################################################
## Change here the parameters for your model                 ##
###############################################################
timeStep = 10 #years
waterDepth = 4000 # meters
L = 1350 # Watt/ms
albedo = 0.3 
epsilon = 1
sigmon = 5.67E-8 #H/m2 K4
years = 100 #years
###############################################################

heatCapacity = waterDepth * 4.2E6 #J/K m2 calculate the heatCapacity
timeYears = [0] #initialization of the years
TK = [400] #initialization of the temperatur 
heatContent = heatCapacity * TK[0] #calculate the first heatContent
heatIn = L * (1 - albedo) / 4 #calculate the heat in temperature
heatOut = 0 #initialization of the out temperature

for i in range(0, years):
	timeYears.append ( timeStep + timeYears[-1])
	heatOut = epsilon * sigmon * pow(TK[-1],4)
	heatContent = heatContent + (heatIn - heatOut) * timeStep * 3.14e7
	TK.append (heatContent / heatCapacity)

print(TK[-1], heatOut)
## Plotting the Graph #########################################
plt.plot(timeYears, TK)
plt.xlabel('Time [Years]', fontsize=12)
plt.ylabel('Temperature [Kelvin]', fontsize=12)
plt.show()