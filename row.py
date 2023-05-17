import numpy as np
import matplotlib.pyplot as plt

def random_uniform(low=5, high=50, size=1):
    return np.random.uniform(low=low, high=high, size=size)

#random_numbers = random_uniform(seed=44, low=5, high=50, size=1000000)
#plt.hist(random_numbers, bins=500)
#plt.show()