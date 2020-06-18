import time
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from three_bodies import Particle


# ---------------------------------------------- Physics
Particle.G = 1
Particle.h = 0.001
Particle.N = 10000
Particle.merge = 0.1
Particle.escape = 100
# ---------------------------------------------- Particles
colors = ['blue','green','red','cyan','magenta','black']
theta_range = (0, 2*np.pi)
radius_range = (30, 36)
velocity_range = (170, 200)
mass_range = (0, 50)
names = 'a'*150
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
    print(particle.name, particle.mass)
# ----------------------------------------------- Plot
axis = 15

fig = plt.figure()
ax1 = plt.axes(xlim=(-int(coord_range)*30, int(coord_range)*30),
               ylim=(-int(coord_range)*30, int(coord_range)*30))
line, = ax1.plot([], [], lw=2)
plt.xlabel('X')
plt.ylabel('Y')

Writer = animation.writers['ffmpeg']
writer = Writer(fps=35, metadata=dict(artist='Me'), bitrate=1800)

plotlays = [len(particles)]
plotcols = [
    colors[i] for i in [
        random.randrange(0,len(colors)) for _ in range(0, len(particles) + 1)
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

print('Creating animation ...')
anim.save('lines.mp4', writer=writer)
# im_ani.save('im.mp4', writer=writer)
# plt.savefig("anim.png")
