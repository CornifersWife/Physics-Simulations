import numpy as np
import matplotlib.pyplot as plt


class Point:
    def __init__(self, mass, x=0, y=0, vx=0, vy=0, ax=0, ay=0, q=0):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.q = q
    def calc_x(self, dt, improved):
        self.x += self.calc_vx(improved * dt, 0) * dt
        return self.x

    def calc_y(self, dt, improved):
        self.y += self.calc_vy(improved * dt, 0) * dt
        return self.y

    def calc_vx(self, dt, improved):
        return self.vx + self.calc_ax(improved * dt, self.q) * dt

    def calc_vy(self, dt, improved):
        return self.vy + self.calc_ay(improved * dt, self.q) * dt

    def calc_ax(self, dt, q):
        return (self.mass * self.ax - (q * self.vx)) / self.mass

    def calc_ay(self, dt, q):
        return (self.mass * self.ay - (q * self.vy)) / self.mass


    def euler_formula(self, fx, fy, dt, time, q):
        x, vx, ax, y, vy, ay = self.x, self.vx, self.ax, self.y, self.vy, self.ay
        # improved = red
        improved = 1 / 2

        steps = time / dt
        self.q = q
        self.ax = fx / self.mass
        self.ay = fy / self.mass
        times = [0]
        x_positions = [self.x]
        y_positions = [self.y]

        for moment in range(int(steps)):
            #print(f'x:{self.x}\tvx:{self.vx}\tax:{self.ax}\n'
            #     f'y:{self.y}\tvy:{self.vy}\tay:{self.ay}\n')
            times.append((times[-1] + dt))
            self.x = self.calc_x(dt, improved)
            self.y = self.calc_y(dt, improved)
            self.vx = self.calc_vx(dt, improved)
            self.vy = self.calc_vy(dt, improved)
            x_positions.append(self.x)
            y_positions.append(self.y)

        interp_t = np.linspace(0, times[-1], len(x_positions))
        interp_x_positions = np.interp(interp_t, times, x_positions)
        interp_y_positions = np.interp(interp_t, times, y_positions)
        plt.plot(interp_x_positions, interp_y_positions, color='#F5A9B8', alpha=0.8)

        self.x, self.vx, self.ax, self.y, self.vy, self.ay = x, vx, ax, y, vy, ay

        # not improved = blue
        improved = 0

        steps = time / dt
        self.q = q
        self.ax = fx / self.mass
        self.ay = fy / self.mass
        times = [0]
        x_positions = [self.x]
        y_positions = [self.y]

        for moment in range(int(steps)):
            #print(f'x:{self.x}\tvx:{self.vx}\tax:{self.ax}\n'
            #      f'y:{self.y}\tvy:{self.vy}\tay:{self.ay}\n')
            times.append((times[-1] + dt))
            self.x = self.calc_x(dt, improved)
            self.y = self.calc_y(dt, improved)
            self.vx = self.calc_vx(dt, improved)
            self.vy = self.calc_vy(dt, improved)

            x_positions.append(self.x)
            y_positions.append(self.y)

        interp_t = np.linspace(0, times[-1], len(x_positions))
        interp_x_positions = np.interp(interp_t, times, x_positions)
        interp_y_positions = np.interp(interp_t, times, y_positions)
        plt.plot(interp_x_positions, interp_y_positions, color='#5BCEFA', alpha=0.8)

        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.title('Projectile Trajectory')
        plt.show()

