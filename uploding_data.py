import matplotlib.pyplot as plt
import numpy as np

''' long way to upload the file

import csv

x = []
y = []

with open('example.txt','r') as csvfile:
     plot = csv.reader(csvfile, delimiter = ',')
     for row in plots:
         x.append(int(row[0]))
         y.append(int(row[1]))

plt.plot(x,y, label ='Data Loaded from file! ')

'''

#second way the short way

x,y = np.loadtxt('example.txt',delimeter=',', unpack=True)
plt.plot(x,y,label='Loaded from file! ')

plt.xlabel('x')
plt.ylabel('x')
plt.title('Intresting Graph\nCheck it out')
plt.legend()
plt.show()
