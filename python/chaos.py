import math
import time
import matplotlib.pyplot as plt
from matplotlib import animation

from three_bodies import Particle


# ---------------------------------------------- Physics
Particle.G = 1
Particle.h = 0.001
Particle.N = 5000
# ---------------------------------------------- Particle 1

# names = 'abc'
# particles = []
# for name in names:
#     particles.append(
#         Particle(
#
#         )
#     )

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


fig = plt.figure()
ax1 = plt.axes(xlim=(-3, 3), ylim=(-3, 3))
line, = ax1.plot([], [], lw=2)
plt.xlabel('X')
plt.ylabel('Y')

plotlays, plotcols = [len(particles)], ["black", "red", "blue"]
lines = []
for index in range(len(particles)):
    lobj = ax1.plot([],[],lw=2,color=plotcols[index])[0]
    lines.append(lobj)

def init():
    for line in lines:
        line.set_data([],[])
    return lines

coord_tuples = [([], []) for _ in range(len(particles))]

def animate(i):
    for index, p in enumerate(particles):
        coord_tuples[index][0].append(p.x_vector[i])
        coord_tuples[index][1].append(p.y_vector[i])

    xlist = [tup[0] for tup in coord_tuples]
    ylist = [tup[1] for tup in coord_tuples]

    for lnum, line in enumerate(lines):
        line.set_data(xlist[lnum][-10:], ylist[lnum][-10:])

    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=range(0, Particle.N, 1),
                               interval=10, blit=True)


plt.show()
