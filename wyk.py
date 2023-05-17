import numpy as np
import matplotlib.pyplot as plt
#scale to odwrotnośc lambda a w tresci projektu nie ma napisane dokładnie ile ona wynosi, moze jest dowolna?
def random_exponential(scale=10, size=1):
    return np.random.exponential(scale=scale, size=size)

#random_numbers = random_exponential(seed=44, scale=0.1, size=1000000)
#plt.hist(random_numbers, bins=1000)
#plt.show()