from matplotlib import pyplot as plt
from CelestialBody import CelestialBody


def poly_movement(x_base, y_base, x_orbiting, y_orbiting):
    for i in range(len(x_orbiting)):
        x_orbiting[i] += x_base[i]
        y_orbiting[i] += y_base[i]
    return x_orbiting, y_orbiting


"""
 Z powodu jak duza jest roznica wielkosci
 w dystansach słońce-ziemia
 kontra ziemia-księżyc
 przy normalnych wymiarach słońca
 ruch księżyca dookoła ziemi jest
 prawie niewidoczny na wykresie

 dlatego jest tutaj opcja   fake_sun
 gdy jest ustawiona na True
 to masa słońce oraz dystans słońce-ziemia
 są parukrotnie zmniejszone,
 dzięki czemu łatwiej jest zauważyć
 ruch księżyca wokół ziemi
"""

##
fake_sun = True

dt = 600
t_max = 3600 * 24 * 366

sun_mass = 1.989e30
distance_sun_earth = 1.5e8
if fake_sun:
    sun_mass /= 1000
    distance_sun_earth /= 10

earth_mass = 5.972e24
distance_earth_moon = 384400
##

earth = CelestialBody(mass_of_orbiting=sun_mass, distance_km=distance_sun_earth)
moon = CelestialBody(mass_of_orbiting=earth_mass, distance_km=distance_earth_moon)

earth_x, earth_y = earth.euler_movement(dt, t_max)
moon_x, moon_y = moon.euler_movement(dt, t_max)

moon_x, moon_y = poly_movement(earth_x, earth_y, moon_x, moon_y)

fig, ax = plt.subplots()

ax.set_aspect('equal')
ax.set_title('Earth and Moon movement')

ax.scatter(earth_x, earth_y, s=1, c='blue', alpha=0.02)
ax.scatter(moon_x, moon_y, s=1, c='grey', alpha=0.02)
ax.scatter(0, 0, s=100, c='Orange')

plt.show()
