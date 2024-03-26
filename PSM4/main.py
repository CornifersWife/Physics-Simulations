# s24435 Maciej Łatosz
import numpy as np

from object import Object
import matplotlib.pyplot as plt

mass = 2
radius = 4
height = 10
alpha = 10
dt = 0.01

kula = Object(radius, "kula", height=height, alpha=alpha)
sfera = Object(radius, "sfera", height=height, alpha=alpha)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

y_ticks = np.arange(0, 2*np.pi+0.5*np.pi, 0.5*np.pi)
y_ticklabels = [f'{i:.1f}π' for i in y_ticks/np.pi]

#       KULA
times, x_positions, y_positions, beta_positions = kula.euler_formula(dt)

y_max = max([max(x_positions), max(y_positions), max(beta_positions)])
y_min = min([min(x_positions), min(y_positions), min(beta_positions)])

# x
axs[0].scatter(times, x_positions, s=1, alpha=0.3, c="blue")
axs[0].set_title('X Positions')

# y
axs[1].scatter(times, y_positions, s=1, alpha=0.3, c="blue")
axs[1].set_title('Y Positions')
axs[1].set_ylim([y_min, y_max * 1.1])

# angle
axs[2].scatter(times, beta_positions, s=1, alpha=0.3, c="blue")
axs[2].set_title('Angle values')
axs[2].set_yticks(y_ticks)
axs[2].set_yticklabels(y_ticklabels)

#       SFERA
times, x_positions, y_positions, beta_positions = sfera.euler_formula(dt)

# x
axs[0].scatter(times, x_positions, s=1, alpha=0.4, c="pink")
axs[0].legend(['Kula', 'Sfera'], markerscale=10)

# y
axs[1].scatter(times, y_positions, s=1, alpha=0.4, c="pink")

# angle
axs[2].scatter(times, beta_positions, s=1, alpha=0.4, c="pink")


plt.show()
