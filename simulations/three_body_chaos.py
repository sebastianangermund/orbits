# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# THREE BODY CHAOS
#
# Vary the initial conditions slightly to get a dramatic change in orbits
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import math

from model import Particle
from utils.plot import plot


# ---------------------------------------------- Physics
Particle.G = 1.002
Particle.h = 0.002
Particle.N = 4000

num_particles = 3
Particle._set_size(num_particles)

# ---------------------------------------------- model

planet_1 = Particle(
    index = 0,
    mass = 100,
    x_pos = 0,
    y_pos = 0,
    x_vel = 5,
    y_vel = 10*(-math.sin((2*math.pi)/3)),
)

planet_2 = Particle(
    index = 1,
    mass = 100,
    x_pos = 1,
    y_pos = 0,
    x_vel = 5,
    y_vel = 10*(math.sin((2*math.pi)/3)),
)

planet_3 = Particle(
    index = 2,
    mass = 100,
    x_pos = 1/2,
    y_pos = math.sin((2*math.pi)/3),
    x_vel = -10 * math.sqrt((1/4+math.pow(math.sin((2*math.pi)/3), 2))),
    y_vel = 0,
)

# ----------------------------------------------- Calculate
number_of_cores = None
for timestep in range(2, Particle.N):
    Particle.run_update(number_of_cores)

# ----------------------------------------------- Plot

# Plot end of simulation only?
plot_start_index = 0
plot_array = Particle.particle_array[:,plot_start_index:]
coord_range = 10
plot_every_nth_step = 4
plot(plot_array, num_particles, coord_range, plot_array.shape[1], plot_every_nth_step)
