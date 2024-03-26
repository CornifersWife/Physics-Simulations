import math


class Struna:
    def __init__(self, length, parts_amount=10):
        self.dx = length / parts_amount
        self.x = [0] * (parts_amount + 1)
        self.y = [0] * (parts_amount + 1)
        self.v = [0] * (parts_amount + 1)
        self.a = [0] * (parts_amount + 1)
        for i in range(1, parts_amount + 1):
            self.x[i] = self.x[i - 1] + self.dx
        for i in range(1, parts_amount):
            self.y[i] = math.sin(self.x[i]) / 1000000

    def calc_position(self, dt, i):
        y_i = self.y[i] + self.calc_v(dt / 2, i) * dt  # self.calc_v(dt / 2, i)*dt
        return y_i

    def calc_v(self, dt, i):
        v_i = self.v[i] + self.a[i] * dt
        return v_i

    def calc_a(self, dt, i):
        # yi-1, yi, yi+1
        y_0, y_1, y_2 = [self.calc_position(dt / 2, i - 1 + j) for j in range(3)]
        a_i = y_0 - 2 * y_1 + y_2
        a_i /= self.dx ** 2
        return a_i

    def kinetic_energy(self):
        out = 0
        for _v in self.v:
            out += self.dx * (_v ** 2)
        out /=2
        return out

    def potential_energy(self):
        out = 0
        for i in range(len(self.y[:-1])):
            out += (self.y[i + 1] - self.y[i]) ** 2
        out /= 2 * self.dx
        return out

    def movement(self, dt, max_t=100):
        times = [0]
        ek = [self.kinetic_energy()]
        ep = [self.potential_energy()]
        ec = [ek[-1] + ep[-1]]

        while times[-1] < max_t:

            for i in range(1, len(self.a[:-1])):
                self.a[i] = self.calc_a(dt, i)

            for i in range(len(self.y)):
                self.y[i] = self.calc_position(dt, i)

            ep.append(self.potential_energy())

            for i in range(len(self.v)):
                self.v[i] = self.calc_v(dt, i)

            ek.append(self.kinetic_energy())
            ec.append(ek[-1] + ep[-1])
            times.append(times[-1] + dt)

        return times, ek, ep, ec
