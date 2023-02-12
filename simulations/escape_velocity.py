# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ROCKET TRIP AROUND THE MOON
#
# Physically "correct" model of a rocket going on a trip around the moon and 
# returning back to earth
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import math

from model import Particle
from plot import plot


## ---- ## ## ---- ## VARIABLES ## ---- ## ## ---- #
 
earth_radius = 6.371 * (10**6) # m
earth_escape_velocity = 11.16 * (10**3) # m/s
earth_mass = 5.972 * (10**24) # kg
earth_coordinate_xy = 0
earth_velocity_xy = 0

moon_mass = 7.348 * (10**22) # kg
moon_coordinate_x = (0.363 * (10**9)) * math.cos(math.pi/6) # m
moon_coordinate_y = (-0.363 * (10**9)) * math.sin(math.pi/6) # m
moon_velocity_x = (1.082 * 10**3) * math.sin(math.pi/6) # m/s
moon_velocity_y = (1.082 * 10**3) * math.cos(math.pi/6) # m/s

rocket_mass = 0
rocket_coordinate_x = earth_radius
rocket_coordinate_y = 0
rocket_velocity_x = earth_escape_velocity
rocket_velocity_y = 0

## ---- ## ## ---- ## SETUP MODEL ## ---- ## ## ---- #

Particle.h = 1
Particle.N = 450000
num_particles = 3
Particle._set_size(num_particles)

earth = Particle(
    index = 0,
    mass = earth_mass,
    x_pos = earth_coordinate_xy,
    y_pos = earth_coordinate_xy,
    x_vel = earth_velocity_xy,
    y_vel = earth_velocity_xy,
)

moon = Particle(
    index = 1,
    mass = moon_mass,
    x_pos = moon_coordinate_x,
    y_pos = moon_coordinate_y,
    x_vel = moon_velocity_x,
    y_vel = moon_velocity_y,
)

rocket = Particle(
    index = 2,
    mass = rocket_mass,
    x_pos = rocket_coordinate_x,
    y_pos = rocket_coordinate_y,
    x_vel = rocket_velocity_x,
    y_vel = rocket_velocity_y,
)

## ---- ## ## ---- ## RUN SIMULATION ## ---- ## ## ---- ##

number_of_cores = None
for timestep in range(2, Particle.N):
    Particle.run_update(number_of_cores)

## ---- ## ## ---- ## RUN PLOT ## ---- ## ## ---- ##

plot_start_index = 0
plot_array = Particle.particle_array[:,plot_start_index:]
coord_range = -2.3*moon_coordinate_y
plot_every_nth_step = 500
plot(plot_array, num_particles, coord_range, plot_array.shape[1], plot_every_nth_step)
