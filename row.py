import numpy as np
import matplotlib.pyplot as plt

def random_uniform(seed, low=0.0, high=1.0, size=1):
    np.random.seed(seed)
    return np.random.uniform(low=low, high=high, size=size)

#random_numbers = random_uniform(seed=44, low=5, high=50, size=1000000)
#plt.hist(random_numbers, bins=1000)
#plt.show()