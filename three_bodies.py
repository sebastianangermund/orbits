#
#  SIMULATE ORBITS OF A PARTICLE SYSTEM USING NEWTONS LAW OF GRAVITY.
#
#  O(h^2)
#
#  sebastian angermund

import weakref
import numpy as np
import multiprocessing as mp


class Particle:
    use_multiprocessing = False
    timestep = 2    # timestep index
    h = 3           # timestep length [seconds]
    N = 300000      # N*timestep = simulation length [seconds]
    G = 6.67e-11    # gravitational constant [SI units]

    def __init__(self, index, mass, x_pos, y_pos, x_vel, y_vel):
        self.index = index
        self.mass = mass
        self.k_array[self.index] = np.power(self.h, 2) * self.G * self.mass
        self.particle_array[self.index*2, 0] = x_pos
        self.particle_array[self.index*2, 1] = x_pos + (self.h * x_vel)
        self.particle_array[self.index*2+1, 0] = y_pos
        self.particle_array[self.index*2+1, 1] = y_pos + (self.h * y_vel)
        if self.use_multiprocessing:
            self._instances.append(self)
        else:
            self._instances.add(weakref.ref(self))

    @classmethod
    def _set_size(cls, num_particles=3):
        cls.num_particles = num_particles
        cls.particle_array = np.zeros((2*num_particles, cls.N), dtype=float)
        cls.k_array = np.zeros(num_particles)
        if num_particles > 2500:
            cls.use_multiprocessing = True
            cls._instances = []
        else:
            cls._instances = set()

    @classmethod
    def _r_update_func(cls, x_step, y_step, delta_x, delta_y, k_list):
        r_sq = np.square(delta_x) + np.square(delta_y)
        r_abs = np.sqrt(r_sq)
        cos = np.divide(np.array(delta_x), r_abs)
        sin = np.divide(np.array(delta_y), r_abs)
        rx = 2 * x_step[0] - (x_step[1] + np.dot(np.divide(np.array(k_list), r_sq), cos))
        ry = 2 * y_step[0] - (y_step[1] + np.dot(np.divide(np.array(k_list), r_sq), sin))
        return rx, ry

    @classmethod
    def _update_positions(cls):
        for ref_1 in cls._instances:
            obj_1 = ref_1()
            x_relevant = cls.particle_array[obj_1.index*2, cls.timestep-1]
            y_relevant = cls.particle_array[obj_1.index*2+1, cls.timestep-1]
            delta_array = np.delete(
                cls.particle_array[:, cls.timestep-1],
                (obj_1.index*2, obj_1.index*2+1),
                axis=0,
            )
            k_list = np.delete(cls.k_array, (obj_1.index))
            delta_x = x_relevant - delta_array[::2]
            delta_y = y_relevant - delta_array[1::2]

            x_step = [x_relevant, cls.particle_array[obj_1.index*2, cls.timestep-2]]
            y_step = [y_relevant, cls.particle_array[obj_1.index*2+1, cls.timestep-2]]

            cls.particle_array[obj_1.index*2, cls.timestep], cls.particle_array[obj_1.index*2+1, cls.timestep] \
                = cls._r_update_func(x_step, y_step, delta_x, delta_y, k_list)

    @classmethod
    def _update_positions_parallel(cls, instance):
        x_relevant = cls.particle_array[instance.index*2, cls.timestep-1]
        y_relevant = cls.particle_array[instance.index*2+1, cls.timestep-1]
        delta_array = np.delete(
            cls.particle_array[:, cls.timestep-1],
            (instance.index*2, instance.index*2+1),
            axis=0,
        )
        k_list = np.delete(cls.k_array, (instance.index))
        delta_x = x_relevant - delta_array[::2]
        delta_y = y_relevant - delta_array[1::2]

        x_step = [x_relevant, cls.particle_array[instance.index*2, cls.timestep-2]]
        y_step = [y_relevant, cls.particle_array[instance.index*2+1, cls.timestep-2]]

        return cls._r_update_func(x_step, y_step, delta_x, delta_y, k_list)

    @classmethod
    def run_update(cls, cores):
        if cls.use_multiprocessing:
            with mp.Pool(cores) as p:
                xy_list = p.map(cls._update_positions_parallel, cls._instances)
            for index, instance in enumerate(cls._instances, 0):
                cls.particle_array[instance.index*2, cls.timestep], cls.particle_array[instance.index*2+1, cls.timestep] = xy_list[index]
        else:
            cls._update_positions()
        cls.timestep += 1
