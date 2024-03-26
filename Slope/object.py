import math


class Object:
    def __init__(self, radius, object_type, alpha=30, height=5, omega=0):

        self.r = radius
        if object_type == "kula":
            self.i = 2 / 5  # po uproszczeniu wzorów   m r^2   się zerują w obliczeniach na przyśpieczenie
        elif object_type == "sfera":
            self.i = 2 / 3
        else:
            print("upsik")
        self.b = 0  # kąt początkowy obiektu
        self.w = omega

        self.alpha = math.radians(alpha)  # kąt nachylenia równi
        self.height = height

        a = 9.86 * math.sin(self.alpha) / (1 + self.i)
        self.ax = a * math.cos(self.alpha)
        self.ay = - a * math.sin(self.alpha)
        self.vx = 0
        self.vy = 0
        self.x = 0
        self.y = self.height + self.r

        self.e = a / self.r

    def calc_v(self, dt):
        vx = self.vx + self.ax * dt
        vy = self.vy + self.ay * dt
        return vx, vy

    def calc_pos(self, dt):
        x = self.x + self.calc_v(dt / 2)[0] * dt
        y = self.y + self.calc_v(dt / 2)[1] * dt
        return x, y

    def calc_beta(self, dt):
        return self.b + self.calc_omega(dt / 2) * dt

    def calc_omega(self, dt):
        return self.w + self.e * dt

    def euler_formula(self, dt):

        times = [0]
        x_positions = [self.x]
        y_positions = [self.y]
        beta_positions = [self.b]
        while self.y >= self.r:
            times.append((times[-1] + dt))
            self.vx = self.calc_v(dt)[0]
            self.vy = self.calc_v(dt)[1]
            self.x = self.calc_pos(dt)[0]
            self.y = self.calc_pos(dt)[1]
            self.w = self.calc_omega(dt)
            self.b = self.calc_beta(dt) % (math.pi * 2)

            x_positions.append(self.x)
            y_positions.append(self.y)
            beta_positions.append(self.b)
        return times, x_positions, y_positions, beta_positions
