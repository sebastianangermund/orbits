import random
import matplotlib.pyplot as plt
from matplotlib import animation


def plot(particles, axees, sim_len):
    fig = plt.figure()
    ax1 = plt.axes(xlim=(-axees, axees),
                   ylim=(-axees, axees))
    line, = ax1.plot([], [], lw=2)
    plt.xlabel('X')
    plt.ylabel('Y')

    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=35, metadata=dict(artist='Me'), bitrate=1800)

    plotlays = [len(particles)]
    colors = ['blue','green','red','cyan','magenta','black']
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
                                   frames=range(0, sim_len, 4),
                                   interval=10, blit=True)

    print('Creating animation ...')
    anim.save('lines.mp4', writer=writer)
