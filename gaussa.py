import numpy as np
import matplotlib.pyplot as plt

def random_gaussian():#size  # ustawienie ziarna
    return np.random.normal(scale=4)#size=size


#random_numbers = random_gaussian_B1(seed=1234, size=1000000)
#plt.hist(random_numbers, bins=1000)
#plt.show()



"""def random_uniform(seed, low=0.0, high=1.0, size=1):
    np.random.seed(seed)
    return np.random.uniform(low=low, high=high, size=size)

random_numbers = random_uniform(seed=1234, low=0, high=10, size=10)"""

