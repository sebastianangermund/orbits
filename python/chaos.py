import math

from three_bodies import Particle
from plot import plot


# ---------------------------------------------- Physics
Particle.G = 1.0001
Particle.h = 0.003
Particle.N = 2000
# ---------------------------------------------- Particle 1
earth = Particle(
    name = 'a',
    mass = 100,
    x_pos = 0,
    y_pos = 0,
    x_vel = 5,
    y_vel = 10*(-math.sin((2*math.pi)/3)),
)
# ---------------------------------------------- Particle 2
moon = Particle(
    name = 'b',
    mass = 100,
    x_pos = 1,
    y_pos = 0,
    x_vel = 5,
    y_vel = 10*(math.sin((2*math.pi)/3)),
)
# ----------------------------------------------- Particle 3
satellite = Particle(
    name = 'c',
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

plot(particles, 6, Particle.N)
