import math


class Force:
    def __init__(self, value, angle_in_degrees):
        self.value = value
        self.angle = math.radians(angle_in_degrees)

    def xy_forces(self):
        fx = self.value * math.cos(self.angle)
        fy = self.value * math.sin(self.angle)

        return fx, fy

    @staticmethod
    def total_force(*forces):
        fx_sum = 0
        fy_sum = 0

        for force in forces:
            fx, fy = force.xy_forces()
            fx_sum += fx
            fy_sum += fy

        value = math.sqrt(fx_sum ** 2 + fy_sum ** 2)
        angle_in_degrees = math.degrees(math.atan2(fy_sum, fx_sum))

        return Force(value, angle_in_degrees)
