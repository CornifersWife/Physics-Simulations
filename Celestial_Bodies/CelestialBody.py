import math


class CelestialBody:
    def __init__(self, mass_of_orbiting, distance_km):

        self.distance = distance_km * 1000

        self.G = 6.67259e-11
        self.M = mass_of_orbiting

        self.x = 0
        self.y = self.distance

        self.vx = math.sqrt(self.G * self.M / self.distance)
        self.vy = 0

        self.ax = 0
        self.ay = 0

    def calc_a_2(self, dt):
        x, y = self.calc_position_2(dt)
        distance = self.calc_distance(x, y)
        a = self.G * self.M / distance ** 2
        ux = -x / distance
        uy = -y / distance
        ax = a * ux
        ay = a * uy
        return ax, ay

    def calc_distance(self, x, y):  # P
        distance = math.sqrt(x ** 2 + y ** 2)
        return distance

    def calc_g(self):
        return self.G * self.M / self.distance

    def calc_position(self, dt):  # x=F y=G
        x = self.x + self.calc_v(dt / 2)[0] * dt
        y = self.y + self.calc_v(dt / 2)[1] * dt
        return x, y

    def calc_position_2(self, dt):
        x = self.x + self.vx * dt / 2
        y = self.y + self.vy * dt / 2
        return x, y

    def calc_v(self, dt):
        vx = self.vx + self.ax * dt
        vy = self.vy + self.ay * dt
        return vx, vy

    def euler_movement(self, dt, t_max):
        time = 0
        x_positions = [self.x]
        y_positions = [self.y]
        curr_percentage = 0
        while time < t_max:
            if time / t_max - curr_percentage > 0.01:
                curr_percentage += 0.01
                print(f'{time * 100 // t_max}%')
            self.distance = self.calc_distance(self.x, self.y)
            self.ax, self.ay = self.calc_a_2(dt)
            self.x, self.y = self.calc_position(dt)
            self.vx, self.vy = self.calc_v(dt)

            time += dt
            x_positions.append(self.x)
            y_positions.append(self.y)
        return x_positions, y_positions
