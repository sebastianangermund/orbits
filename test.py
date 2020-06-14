import weakref

class Aa:
    _instances = set()
    def __init__(self, co):
        self.co = co
        self._instances.add(weakref.ref(self))

    @classmethod
    def update_positions(cls):
        distance_list = []
        for ref_1 in cls._instances:
            obj_1 = ref_1()
            distance_dict = {obj_1: {}}
            for index, ref_2 in enumerate(cls._instances):
                obj_2 = ref_2()
                if obj_1 == obj_2:
                    continue
                distance_dict[obj_1][index] = {'x': obj_1.co, 'y': obj_2.co}
            distance_list.append(distance_dict)
        return distance_list

a = Aa(1)
b = Aa(2)
c = Aa(3)

print(a.update_positions())
