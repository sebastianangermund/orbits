import math
import time
import matplotlib.pyplot as plt

from three_bodies import Particle


# ---------------------------------------------- Particle 1
earth = Particle(
    name = 'Earth',
    mass = 5.97e24,
    x_pos = 0,
    y_pos = 0,
    x_vel = 0,
    y_vel = 0,
)
# ---------------------------------------------- Particle 2
moon = Particle(
    name = 'Moon',
    mass = 50,
    x_pos = 363e6,
    y_pos = 0,
    x_vel = 0,
    y_vel = 1100,
)
# ----------------------------------------------- Particle 3
satellite = Particle(
    name = 'Satellite',
    mass = 0,
    x_pos = -Particle.a,
    y_pos = -Particle.a,
    x_vel = (0.99 * Particle.v) / math.sqrt(2),
    y_vel = 1100,
)

start = time.perf_counter()

for timestep in range(2, Particle.N):
    Particle._update_positions(timestep)

print('calc time: ', time.perf_counter() - start)

plt.plot(earth.x_vector, earth.y_vector, label=earth.name)
plt.plot(moon.x_vector, moon.y_vector, label=moon.name)
plt.plot(satellite.x_vector, satellite.y_vector, label=satellite.name)
plt.legend(loc="upper left")
plt.show()
