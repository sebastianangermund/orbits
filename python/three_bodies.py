#
#  SIMULATE ORBITS OF A THREE BODY SYSTEM (SPECIFICALLY AN
#  EARTH-MOON-SATELLITE SYSTEM) USING NEWTONS LAW OF GRAVITY.
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
    #   N*timestep = simulation length in seconds
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
        # self.x_pos = x_pos
        # self.y_pos = y_pos
        self.x_vector = np.zeros(self.N)
        self.x_vector[0] = x_pos
        self.x_vector[1] = x_pos + (self.h * x_vel)
        self.y_vector = np.zeros(self.N)
        self.y_vector[0] = y_pos
        self.y_vector[1] = y_pos + (self.h * y_vel)
        self._instances.add(weakref.ref(self))

        def __del__(self):
            pass

    @classmethod
    def _r_func(cls, delta_x_list, delta_y_list):
        r_sq = np.square(delta_x_list) + np.square(delta_y_list)
        r_abs = np.sqrt(r_sq)
        return r_sq, r_abs

    @classmethod
    def _rx_func(cls, x_list, delta_x_list, delta_y_list, k_list):
        r_sq, r_abs = cls._r_func(delta_x_list, delta_y_list)
        cos = np.divide(np.array(delta_x_list), r_abs)
        rx = 2 * x_list[0] - (x_list[1] + np.dot(np.divide(np.array(k_list), r_sq), cos))
        return rx

    @classmethod
    def _ry_func(cls, y_list, delta_x_list, delta_y_list, k_list):
        r_sq, r_abs = cls._r_func(delta_x_list, delta_y_list)
        sin = np.divide(np.array(delta_y_list), r_abs)
        ry = 2 * y_list[0] - (y_list[1] + np.dot(np.divide(np.array(k_list), r_sq), sin))
        return ry

    @classmethod
    def _update_positions(cls, timestep):
        distance_list = []
        merged = []
        del_ = []
        for ref_1 in cls._instances:
            obj_1 = ref_1()
            distance_dict = {}
            for index, ref_2 in enumerate(cls._instances):
                obj_2 = ref_2()
                if obj_1 == obj_2:
                    continue
                delta_x = obj_1.x_vector[timestep-1] - obj_2.x_vector[timestep-1]
                delta_y = obj_1.y_vector[timestep-1] - obj_2.y_vector[timestep-1]
                coll = False
                if obj_1 not in merged and obj_1 not in del_ and obj_2 not in merged and obj_2 not in del_:
                    if math.sqrt(delta_x**2 + delta_y**2) <= cls.merge:
                        coll = True
                        merged.append(obj_1)
                        if obj_2 not in merged:
                            merged.append(obj_2)
                    elif abs(obj_1.x_vector[timestep-1]) > cls.escape or abs(obj_1.y_vector[timestep-1]) > cls.escape:
                        if obj_1 not in merged:
                            del_.append(obj_1)

                distance_dict[index] = {
                    'x': delta_x, 'y': delta_y, 'k': obj_2.K, 'coll': coll,
                }
            distance_list.append((obj_1, distance_dict))

        for object in distance_list:
            relations = [di for key, di in object[1].items()]
            coll_list = [di['coll'] for di in relations]
            if True in coll_list:
                object[0].x_vector[timestep] = \
                    object[0].x_vector[timestep - 1] \
                    + (object[0].x_vector[timestep - 1] - object[0].x_vector[timestep - 2])/3
                object[0].y_vector[timestep] = \
                    object[0].y_vector[timestep - 1] \
                    + (object[0].y_vector[timestep - 1] - object[0].y_vector[timestep - 1])/3
                continue
            delta_x_list = [di['x'] for di in relations]
            delta_y_list = [di['y'] for di in relations]
            k_list = [di['k'] for di in relations]

            x_list = [object[0].x_vector[timestep-1], object[0].x_vector[timestep-2]]
            y_list = [object[0].y_vector[timestep-1], object[0].y_vector[timestep-2]]

            object[0].x_vector[timestep] = cls._rx_func(x_list, delta_x_list, delta_y_list, k_list)
            object[0].y_vector[timestep] = cls._ry_func(y_list, delta_x_list, delta_y_list, k_list)

        for i, ob in enumerate(merged[::2]):
            ob_2 = merged[i+1]
            ob.mass += ob_2.mass
            ob.K = math.pow(ob.h, 2) * ob.G * ob.mass
            del_.append(ob_2)

        for ob in del_:
            cls._instances.remove(weakref.ref(ob))
            del ob
