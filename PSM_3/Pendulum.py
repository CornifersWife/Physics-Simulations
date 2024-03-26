import math

import numpy as np


class Pendulum:
    def __init__(self, l, alpha=130, g=9.81):
        self.alpha = math.radians(alpha)
        self.l = l
        self.g = g
        self.omega = 0
        self.epsilon = (-math.sin(self.alpha) * self.g) / self.l

    def calc_alpha(self, dt, improved):
        if improved:
            return self.alpha + self.calc_omega(dt / 2) * dt
        else:
            return self.alpha + self.omega * dt

    def calc_omega(self, dt):
        return self.omega + self.epsilon * dt

    def calc_epsilon(self):
        return (-math.sin(self.alpha) * self.g) / self.l

    def calc_kna(self, kna, dt):
        return self.alpha + kna * dt

    def calc_knw(self, knw, dt):
        return self.omega + knw * dt

    def calc_epsilon_RK4(self, alpha):
        return (-math.sin(alpha) * self.g) / self.l

    def coordinates(self):
        x = self.l * math.cos(self.alpha - (math.pi / 2))
        y = self.l * math.sin(self.alpha - (math.pi / 2))

        return x, y

    def PP(self, kna, knw):
        return knw, self.calc_epsilon_RK4(kna)

    def rk4_step(self, dt):
        k1a, k1w = self.PP(self.alpha, self.omega)
        k2a, k2w = self.PP(self.calc_kna(k1a, dt / 2), self.calc_knw(k1w, dt / 2))
        k3a, k3w = self.PP(self.calc_kna(k2a, dt / 2), self.calc_knw(k2w, dt / 2))
        k4a, k4w = self.PP(self.calc_kna(k3a, dt), self.calc_knw(k3w, dt))

        self.alpha += (1 / 6) * (k1a + 2 * k2a + 2 * k3a + k4a) * dt
        self.omega += (1 / 6) * (k1w + 2 * k2w + 2 * k3w + k4w) * dt

    def rk4_formula(self, dt, time):
        steps = time / dt
        times = [0]
        x_positions = [self.coordinates()[0]]
        y_positions = [self.coordinates()[1]]
        for moment in range(int(steps)):
            times.append((times[-1] + dt))
            self.epsilon = self.calc_epsilon()
            self.rk4_step(dt)
            print(self.coordinates())
            print(f'E: {self.epsilon}\t w: {self.omega}\t a:{math.degrees(self.alpha)}')

            x_positions.append(self.coordinates()[0])
            y_positions.append(self.coordinates()[1])
        interp_t = np.linspace(0, times[-1], len(x_positions))
        return times, interp_t, x_positions, y_positions

    def euler_formula(self, dt, time, improved=False):

        steps = time / dt
        times = [0]
        x_positions = [self.coordinates()[0]]
        y_positions = [self.coordinates()[1]]

        for moment in range(int(steps)):
            times.append((times[-1] + dt))
            self.epsilon = self.calc_epsilon()
            self.omega = self.calc_omega(dt)
            self.alpha = self.calc_alpha(dt, improved)

            x_positions.append(self.coordinates()[0])
            y_positions.append(self.coordinates()[1])
        interp_t = np.linspace(0, times[-1], len(x_positions))
        return times, interp_t, x_positions, y_positions
