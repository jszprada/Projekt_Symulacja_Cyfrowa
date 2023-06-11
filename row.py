import numpy as np
import matplotlib.pyplot as plt


class RandomUniformGenerator:
    def __init__(self, seed=None, low=5, high=50):
        self.rng = np.random.default_rng(seed)
        self.low = low
        self.high = high

    def generate(self, size=None):
        return self.rng.uniform(low=self.low, high=self.high, size=size)

    def __call__(self, size=None):
        return self.generate(size)


# Użycie klasy
"""generator = RandomUniformGenerator(seed=42, low=5, high=50)
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
