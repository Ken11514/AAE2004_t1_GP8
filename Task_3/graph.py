import matplotlib.pyplot as plt
import numpy as np
# Bar chart
'''
fuel_cost = [2724,5448,5448]
time_cost = [1698,1852,2316]
fixed_cost = [2000,2500,2500]
total_cost = [77064,98003,71844]
index = np.arange(3)
label = ['Model 1','Model 2','Model 3']
p1 = [6422,9800,10264]
p2 =[3698,4352,4816]
p3 = [2000,2500,2500]
#plt.bar(index ,p1,color='red',label='fuel cost' )
#plt.bar(index,p2,color='blue',label='time cost')
#plt.bar(index,p3,color='green',label='fixed cost')
plt.bar(index,total_cost,color='orange',label='total cost')
plt.legend()
plt.ylabel('cost ($)')
plt.xticks(index,['Model 1','Model 2','Model 3'])
plt.title('Total flight cost for each Model')
plt.savefig('images/Flight cost for each Model .png')
plt.show()

ox, oy = [], []
for i in range(-10, 60): # draw the buttom border 
    ox.append(i)
    oy.append(0)
    ox.append(i)
    oy.append(30)

plt.plot(ox, oy, "sk") # plot the obstacle
plt.show()
'''
