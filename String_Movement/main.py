import math

from matplotlib import pyplot as plt

from struna import Struna

length = math.pi  # L
numb = 10  # N

dt = 0.01
max_t = 10

fig, ax = plt.subplots()

struna = Struna(length, numb)

times, ek, ep, ec = struna.movement(dt, max_t)

ax.plot(times, ek, alpha=0.3, c='red')
ax.plot(times, ep, alpha=0.3, c='blue')
ax.plot(times, ec, alpha=0.3, c='purple')
ax.legend(['Ek', 'Ep', 'Ec'], markerscale=10)

plt.show()
