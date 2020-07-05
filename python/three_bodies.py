#
#  SIMULATE ORBITS OF AN N BODY SYSTEM USING NEWTONS LAW OF GRAVITY.
#
#  O(h^2)
#
#  sebastian angermund

import math
import weakref
import numpy as np


class Particle:
    _instances = set()
    #  Time step [seconds]
    h = 3
    #   N*timestep = simulation length in seconds * h
    N = 300000
    #  Gravitational constant [SI units]
    G = 6.67e-11
    #  Earth radius [m]
    R = 6.571e6
    #  Moon radius [m]
    Rmoon = 3.737e6
    #  Merge objects at some distance
    merge = R + Rmoon
    # Remove object that escape
    escape = merge ** 3
    #  Coordinate constant
    a = R/math.sqrt(2)
    #  Earth escape velocity [m/s]
    escV = 11e3
    #  Satellite initial absolute velocity (scale the escape velocity)
    v = 1.0 * escV

    def __init__(self, mass, x_pos, y_pos, x_vel, y_vel, name=''):
        self.name = name
        self.mass = mass
        self.K = math.pow(self.h, 2) * self.G * self.mass
        self.x_vector = np.zeros(self.N)
        self.x_vector[0] = x_pos
        self.x_vector[1] = x_pos + (self.h * x_vel)
        self.y_vector = np.zeros(self.N)
        self.y_vector[0] = y_pos
        self.y_vector[1] = y_pos + (self.h * y_vel)
        self._instances.add(weakref.ref(self))

    @classmethod
    def _r_update_func(cls, x_list, y_list, delta_x_list, delta_y_list, k_list):
        r_sq = np.square(delta_x_list) + np.square(delta_y_list)
        r_abs = np.sqrt(r_sq)
        cos = np.divide(np.array(delta_x_list), r_abs)
        sin = np.divide(np.array(delta_y_list), r_abs)
        rx = 2 * x_list[0] - (x_list[1] + np.dot(np.divide(np.array(k_list), r_sq), cos))
        ry = 2 * y_list[0] - (y_list[1] + np.dot(np.divide(np.array(k_list), r_sq), sin))
        return rx, ry

    @classmethod
    def _update_positions(cls, timestep):
        update_list = []
        for ref_1 in cls._instances:
            obj_1 = ref_1()
            delta_x_list = []
            delta_y_list = []
            k_list = []
            delta_list = [obj_1, delta_x_list, delta_y_list, k_list]
            for ref_2 in cls._instances:
                obj_2 = ref_2()
                if obj_1 == obj_2:
                    continue
                delta_x = obj_1.x_vector[timestep-1] - obj_2.x_vector[timestep-1]
                delta_y = obj_1.y_vector[timestep-1] - obj_2.y_vector[timestep-1]

                delta_list[1].append(delta_x)
                delta_list[2].append(delta_y)
                delta_list[3].append(obj_2.K)

            update_list.append(delta_list)

        for delta_list in update_list:
            x_list = [delta_list[0].x_vector[timestep-1], delta_list[0].x_vector[timestep-2]]
            y_list = [delta_list[0].y_vector[timestep-1], delta_list[0].y_vector[timestep-2]]

            delta_list[0].x_vector[timestep], delta_list[0].y_vector[timestep] \
                = cls._r_update_func(x_list, y_list, delta_list[1], delta_list[2], delta_list[3])
