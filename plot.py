import random
import time
import matplotlib.pyplot as plt
from matplotlib import animation


def plot(particle_array, num_particles, axees, sim_len, plot_step):
    """Copy pasted potato code"""
    fig = plt.figure()
    ax1 = plt.axes(xlim=(-axees, axees),
                   ylim=(-axees, axees))
    _, = ax1.plot([], [], lw=2)
    plt.xlabel('X')
    plt.ylabel('Y')

    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=35, metadata=dict(artist='Me'), bitrate=1800)

    colors = ['blue','green','red','cyan','magenta','black','yellow']
    lines = []
    for _ in range(num_particles):
        lobj = ax1.plot([],[],lw=2,color=colors[random.randrange(0,len(colors))])[0]
        lines.append(lobj)

    def init():
        for line in lines:
            line.set_data([],[])
        return lines

    coord_tuples = [([], []) for _ in range(num_particles)]

    def animate(i):
        for index in range(0, num_particles):
            coord_tuples[index][0].append(particle_array[2*index, i])
            coord_tuples[index][1].append(particle_array[2*index+1, i])

        xlist = [tup[0] for tup in coord_tuples]
        ylist = [tup[1] for tup in coord_tuples]

        for lnum, line in enumerate(lines):
            line.set_data(xlist[lnum][-5:], ylist[lnum][-5:])

        return lines

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=range(0, sim_len, plot_step),
                                   interval=10, blit=True)
    start = time.perf_counter()
    print('Creating animation ...\n')
    anim.save('simulation.mp4', writer=writer)
    calc_time = time.perf_counter() - start
    print(f'animation time: {calc_time} s\n')
