import math

from three_bodies import Particle
from plot import plot


# ---------------------------------------------- Physics
Particle.G = 1.003
Particle.h = 0.002
Particle.N = 3000

num_particles = 3
Particle._set_size(num_particles)
# ---------------------------------------------- Particle 1
earth = Particle(
    index = 0,
    mass = 100,
    x_pos = 0,
    y_pos = 0,
    x_vel = 5,
    y_vel = 10*(-math.sin((2*math.pi)/3)),
)
# ---------------------------------------------- Particle 2
moon = Particle(
    index = 1,
    mass = 100,
    x_pos = 1,
    y_pos = 0,
    x_vel = 5,
    y_vel = 10*(math.sin((2*math.pi)/3)),
)
# ----------------------------------------------- Particle 3
satellite = Particle(
    index = 2,
    mass = 100,
    x_pos = 1/2,
    y_pos = math.sin((2*math.pi)/3),
    x_vel = -10 * math.sqrt((1/4+math.pow(math.sin((2*math.pi)/3), 2))),
    y_vel = 0,
)
particles = [earth, moon, satellite]
# ----------------------------------------------- Calculate

for timestep in range(2, Particle.N):
    Particle._update_positions(timestep)

# ----------------------------------------------- Plot

plot(Particle.particle_array, num_particles, 10, Particle.N)
