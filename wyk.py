import numpy as np
import matplotlib.pyplot as plt
#scale to odwrotnośc lambda a w tresci projektu nie ma napisane dokładnie ile ona wynosi, moze jest dowolna?
def random_exponential(seed, scale=1.0, size=1):
    np.random.seed(seed)
    return np.random.exponential(scale=scale, size=size)

#random_numbers = random_exponential(seed=44, scale=1, size=1000000)
#plt.hist(random_numbers, bins=1000)
#plt.show()