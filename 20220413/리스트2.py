import math
import matplotlib.pyplot as plt

sine = [math.sin(2*math.pi*x/100)for x in range(100)]

plt.plot(sine)
plt.show()