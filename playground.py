import time
import random
import numpy as np

from plot import plot
from three_bodies import Particle


# ------------------------------------------- EDIT

# sim variables
simulation_step_length = 0.04
simulation_steps = 500
gravitational_constant = 1

# particle variables
theta_range = (0, 2*np.pi)
radius_range = (25, 200)
velocity_range = (300, 400)
mass_range = (10, 50)
sun_mass = 10**5
num_of_particles = 10

# ------------------------------------------- DON'T EDIT
Particle.G = gravitational_constant
Particle.h = simulation_step_length
Particle.N = simulation_steps
Particle._set_size(num_of_particles)

particles = []

sun = Particle(
    index = 0,
    mass = sun_mass,
    x_pos = 0,
    y_pos = 0,
    x_vel = 0,
    y_vel = 0,
)
particles.append(sun)

for index in range(1, num_of_particles):
    radius = random.uniform(radius_range[0], radius_range[1])
    theta = random.uniform(theta_range[0], theta_range[1])
    vel = random.randrange(velocity_range[0], velocity_range[1])/np.sqrt(radius)
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

number_of_cores = None # None defaults to os.cpu_count()

start = time.perf_counter()
print(f'\nCalculating... Updating {num_of_particles} particle positions {Particle.N} times.\n')

for timestep in range(2, Particle.N):
    Particle.run_update(number_of_cores)

calc_time = time.perf_counter() - start

print(f'calc time: {calc_time} s\n')
print(f'Calc time/step was {calc_time/Particle.N} s\n')

# ----------------------------------------------- Plot

# Plot end of simulation only?
plot_start_index = 90
plot_array = Particle.particle_array[:,plot_start_index:]
coord_range = 350
plot_every_nth_step = 2
plot(plot_array, num_of_particles, coord_range, plot_array.shape[1], plot_every_nth_step)
