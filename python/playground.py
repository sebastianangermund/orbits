import math
import time
import matplotlib.pyplot as plt
from matplotlib import animation
from random import randrange

from three_bodies import Particle


# ---------------------------------------------- Physics
Particle.G = 1
Particle.h = 0.001
Particle.N = 5000
Particle.merge = 0.1
# ---------------------------------------------- Particles
colors = ['blue','green','red','cyan','magenta','black']
velocity_range = (-20, 20)
mass_range = (0, 110)
names = 'a'*90
particles = []
coord_range = 6
for name in names:
    particles.append(
        Particle(
            name = name,
            mass = randrange(mass_range[0], mass_range[1]),
            x_pos = randrange(-coord_range, coord_range),
            y_pos = randrange(-coord_range, coord_range),
            x_vel = randrange(velocity_range[0], velocity_range[1]),
            y_vel = randrange(velocity_range[0], velocity_range[1]),
        )
    )

# ----------------------------------------------- Calculate

start = time.perf_counter()

for timestep in range(2, Particle.N):
    Particle._update_positions(timestep)

print('calc time: ', time.perf_counter() - start)
# ----------------------------------------------- Plot

axis = 15

fig = plt.figure()
ax1 = plt.axes(xlim=(-int(coord_range)*20, int(coord_range)*20),
               ylim=(-int(coord_range)*20, int(coord_range)*20))
line, = ax1.plot([], [], lw=2)
plt.xlabel('X')
plt.ylabel('Y')

plotlays = [len(particles)]
plotcols = [
    colors[i] for i in [
        randrange(0,len(colors)) for _ in range(0, len(particles) + 1)
    ]
]

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
                               frames=range(0, Particle.N, 4),
                               interval=10, blit=True)


plt.show()
