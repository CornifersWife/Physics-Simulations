#Irys Łatosz
from Pendulum import Pendulum
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def show_movement(ax,times, interp_t, x_positions, y_positions, color='#F5A9B8', name="Projectile trajectory"):
    ax.set_xlim(min(x_positions) * 1.5, max(x_positions) * 1.5)
    ax.set_ylim(min(y_positions) * 1.5, max(y_positions) * 1.5)
    ax.set_aspect('equal')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_title(name)
    line, = ax.plot([], [], 'o', color=color, markersize=1)
    start, = ax.plot([], [], 'o', color='black', markersize=10)
    end, = ax.plot([], [], 'o', color=color, markersize=6)
    line_between_points, = ax.plot([], [], color=color, alpha=0.5)

    def animate(i):
        interp_x_positions = np.interp(interp_t[:i + 1], times, x_positions)
        interp_y_positions = np.interp(interp_t[:i + 1], times, y_positions)
        line.set_data(interp_x_positions, interp_y_positions)
        start.set_data([0], [0])
        end.set_data([interp_x_positions[-1]], [interp_y_positions[-1]])
        line_between_points.set_data([0, interp_x_positions[-1]], [0, interp_y_positions[-1]])

    ani = FuncAnimation(fig, animate, frames=len(interp_t), interval=33, repeat=False)
    return ani
##parameters
dt = 0.3
time = 100
pendulum_length = 2
angle = 170
fig, axs = plt.subplots(1, 3, figsize=(18, 6))


p1 = Pendulum(pendulum_length, angle)
p2 = Pendulum(pendulum_length, angle)
p3 = Pendulum(pendulum_length, angle)
res_normal = p2.euler_formula(dt, time)
res_imp = p1.euler_formula(dt, time, True)
res_rk4 = p3.rk4_formula(dt, time)

ani1 = show_movement(axs[0], *res_normal, color="#303088",name='Eulers')  # Normal, blue
ani2 = show_movement(axs[1], *res_imp, color='#F5A9B8',name='Eulers_improved')  # Improved, pink
ani3 = show_movement(axs[2], *res_rk4, color="#308830",name='rk4')  # rk green
plt.tight_layout()
plt.show()
