import time
import random
import numpy as np

from plot import plot
from three_bodies import Particle


# ---------------------------------------------- Physics
Particle.G = 1
Particle.h = 0.002
Particle.N = 10000
Particle.merge = 0.1
Particle.escape = 100
# ---------------------------------------------- Particles
theta_range = (0, 2*np.pi)
radius_range = (28, 38)
velocity_range = (170, 220)
mass_range = (0, 50)
names = 'a'*75
coord_range = 6
particles = []

sun = Particle(
    name = 'sun',
    mass = 10**6,
    x_pos = 0,
    y_pos = 0,
    x_vel = 0,
    y_vel = 0,
)
particles.append(sun)

for name in names:
    radius = random.uniform(radius_range[0], radius_range[1])
    theta = random.uniform(theta_range[0], theta_range[1])
    vel = random.randrange(velocity_range[0], velocity_range[1])
    x_pos, y_pos = radius * np.cos(theta), radius * np.sin(theta)
    x_vel, y_vel = vel * np.sin(theta), - vel * np.cos(theta)
    particles.append(
        Particle(
            name = name,
            mass = random.randrange(mass_range[0], mass_range[1]),
            x_pos = x_pos,
            y_pos = y_pos,
            x_vel = x_vel,
            y_vel = y_vel,
        )
    )

# ----------------------------------------------- Calculate

start = time.perf_counter()

for timestep in range(2, Particle.N):
    Particle._update_positions(timestep)

print('calc time: ', time.perf_counter() - start)

for particle in Particle._instances:
    particle = particle()
    print(particle.name, particle.mass)
# ----------------------------------------------- Plot

plot(particles, int(coord_range)*40, Particle.N)
