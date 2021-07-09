import numpy as np
import matplotlib.pyplot as plt
import random as rnd

dev_x = np.arange(1, 101, 1)
dev_y = np.random.randn(100)

plt.plot(dev_x, dev_y)

plt.show()
