import time
import random
import numpy as np

from plot import plot
from three_bodies import Particle


# ---------------------------------------------- Physics
Particle.G = 1
Particle.h = 0.004
Particle.N = 10000
Particle.merge = 0.1
Particle.escape = 100
# ---------------------------------------------- Particles
num_particles = 150
Particle._set_size(num_particles)

theta_range = (0, 2*np.pi)
radius_range = (28, 45)
velocity_range = (165, 220)
mass_range = (0, 50)
indexes = list(range(1, num_particles))
particles = []

sun = Particle(
    index = 0,
    mass = 10**6,
    x_pos = 0,
    y_pos = 0,
    x_vel = 0,
    y_vel = 0,
)
particles.append(sun)

for index in indexes:
    radius = random.uniform(radius_range[0], radius_range[1])
    theta = random.uniform(theta_range[0], theta_range[1])
    vel = random.randrange(velocity_range[0], velocity_range[1])
    x_pos, y_pos = radius * np.cos(theta), radius * np.sin(theta)
    x_vel, y_vel = vel * np.sin(theta), - vel * np.cos(theta)
    particles.append(
        Particle(
            index = index,
            mass = random.randrange(mass_range[0], mass_range[1]),
            x_pos = x_pos,
            y_pos = y_pos,
            x_vel = x_vel,
            y_vel = y_vel,
        )
    )

# ----------------------------------------------- Calculate

start = time.perf_counter()
print(f'\nCalculating... Updating {num_particles} particles position {Particle.N} times.\n')

for timestep in range(2, Particle.N):
    Particle._update_positions(timestep)

calc_time = time.perf_counter() - start

print(f'calc time: {calc_time}\n')
print(f'Calc time/step was approximately {calc_time/Particle.N} s\n')

# for particle in Particle._instances:
#     particle = particle()
#     print(particle.index, particle.mass)
# ----------------------------------------------- Plot

# Plot M last steps of simulation
M = 2000
plot_array = Particle.particle_array[:,M:]

coord_range = 6
plot(plot_array, num_particles, int(coord_range)*40, M)
