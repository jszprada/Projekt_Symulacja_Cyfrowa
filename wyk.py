import numpy as np
import matplotlib.pyplot as plt


class RandomExponentialGenerator:
    def __init__(self, seed=None, scale=10):
        self.rng = np.random.default_rng(seed)
        self.scale = scale

    def generate(self, size=None):
        return self.rng.exponential(scale=self.scale, size=size)

    def __call__(self, size=None):
        return self.generate(size)


"""generator = RandomExponentialGenerator(seed=42,scale=1250)
num_variables = 1000000  # Liczba zmiennych losowych
data = []

for _ in range(num_variables):
    random_value = generator()
    data.append(random_value)

# Wykres histogramu
plt.hist(data, bins='auto')
plt.xlabel('Wartość')
plt.ylabel('Liczebność')
plt.title('Histogram zmiennych losowych')
plt.show()"""
