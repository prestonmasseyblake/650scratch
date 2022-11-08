import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import random as rd
from itertools import combinations, groupby
# y = [0, 1, 1, 3, 16, 9.999999999999993, 40.000000000000014]
y = [0, 0, 0, 1.0000000000000018, 0.9999999999999982, 2, 2.9999999999999964]
x =  [10,100,500,1000,5000,10000,50000]
plt.plot(x, y)
plt.title('Makeways CoinChange Runtime O(n * m) Changing amounts and keeping coins at 1 through 100')
plt.ylabel('time in miliseconds')
plt.xlabel('Size of Coins 1 through 100 and amount = val')
plt.show()
