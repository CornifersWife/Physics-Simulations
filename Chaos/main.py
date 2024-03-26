from point import Point
import matplotlib.pyplot as plt

time = 25
dt = 0.03
# point_euler = Point(dt=dt)
point_midpoint = Point(dt=dt)
point_RK4 = Point(dt=dt)
point_RK4_prec = Point(dt=dt)

fig, axs = plt.subplots(3, 1)

# xs,ys,zs = point_euler.euler_formula(time)
# xs,ys,zs = point_euler.euler_formula(time)

# axs[0][0].plot(xs,zs, alpha=0.3, c='red')

xs, ys, zs = point_midpoint.euler_formula(time)

axs[0].plot(xs, zs, alpha=0.3, c='red')

xs, ys, zs = point_RK4_prec.euler_formula2(time)

axs[1].plot(xs, zs, alpha=0.3, c='purple')

xs, ys, zs = point_RK4.rk4_formula(time)

axs[2].plot(xs, zs, alpha=0.3, c='blue')

plt.show()
