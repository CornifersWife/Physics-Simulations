class Point:
    def __init__(self, x0=1, y0=1, z0=1, A=10, B=25, C=8 / 3, dt=0.03):
        self.A = A
        self.B = B
        self.C = C
        self.dt = dt
        self.x = x0
        self.y = y0
        self.z = z0

    def calc_dx(self):
        return self.A * (self.y - self.x)

    def calc_dy(self):
        return self.x * (self.B - self.z) - self.y

    def calc_dz(self):
        return self.x * self.y - self.C * self.z

    def euler_formula(self, time=100):
        steps = time / self.dt
        x_positions = [self.x]
        y_positions = [self.y]
        z_positions = [self.z]
        for _ in range(int(steps)):
            dx = self.calc_dx()
            dy = self.calc_dy()
            dz = self.calc_dz()
            self.x += dx * self.dt
            self.y += dy * self.dt
            self.z += dz * self.dt
            x_positions.append(self.x)
            y_positions.append(self.y)
            z_positions.append(self.z)

        return x_positions, y_positions, z_positions

    def calc_dx2(self):
        return self.A * (self.temp_y() - self.temp_x())

    def calc_dy2(self):
        return self.temp_x() * (self.B - self.temp_z()) - self.temp_y()

    def calc_dz2(self):
        return self.temp_x() * self.temp_y() - self.C * self.temp_z()

    def temp_x(self):
        return self.x + self.calc_dx() * self.dt / 2

    def temp_y(self):
        return self.y + self.calc_dy() * self.dt / 2

    def temp_z(self):
        return self.z + self.calc_dz() * self.dt / 2

    def euler_formula2(self, time=100):
        steps = time / self.dt
        x_positions = [self.x]
        y_positions = [self.y]
        z_positions = [self.z]
        for _ in range(int(steps)):
            dx = self.calc_dx2()
            dy = self.calc_dy2()
            dz = self.calc_dz2()
            self.x += dx * self.dt
            self.y += dy * self.dt
            self.z += dz * self.dt
            x_positions.append(self.x)
            y_positions.append(self.y)
            z_positions.append(self.z)

        return x_positions, y_positions, z_positions

    # RK4============================

    def calc_knx(self, knx, dt):
        return self.x + knx * dt

    def calc_kny(self, kny, dt):
        return self.y + kny * dt

    def calc_knz(self, knz, dt):
        return self.z + knz * dt

    def calc_dx3(self, x, y, z):
        return self.A * (y - x)

    def calc_dy3(self, x, y, z):
        return x * (self.B - z) - y

    def calc_dz3(self, x, y, z):
        return x * y - self.C * z

    def PP(self, x, y, z):
        return self.calc_dx3(x, y, z), self.calc_dy3(x, y, z), self.calc_dz3(x, y, z)

    def rk4_step(self):
        k1x, k1y, k1z = self.PP(self.x, self.y, self.z)
        k2x, k2y, k2z = self.PP(self.calc_knx(k1x, self.dt / 2), self.calc_kny(k1y, self.dt / 2),
                                self.calc_knz(k1z, self.dt / 2))
        k3x, k3y, k3z = self.PP(self.calc_knx(k2x, self.dt / 2), self.calc_kny(k2y, self.dt / 2),
                                self.calc_knz(k2z, self.dt / 2))
        k4x, k4y, k4z = self.PP(self.calc_knx(k3x, self.dt), self.calc_kny(k2y, self.dt), self.calc_knz(k3z, self.dt))

        self.x += (1 / 6) * (k1x + 2 * k2x + 2 * k3x + k4x) * self.dt
        self.y += (1 / 6) * (k1y + 2 * k2y + 2 * k3y + k4y) * self.dt
        self.z += (1 / 6) * (k1z + 2 * k2z + 2 * k3z + k4z) * self.dt

    def rk4_formula(self, time=100):
        steps = time / self.dt
        x_positions = [self.x]
        y_positions = [self.y]
        z_positions = [self.z]
        for moment in range(int(steps)):
            self.rk4_step()
            x_positions.append(self.x)
            y_positions.append(self.y)
            z_positions.append(self.z)
        return x_positions, y_positions, z_positions
