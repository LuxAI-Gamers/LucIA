from bh_trees import Task


class Pillage(Task):


    def _init_(self):
        super(Pillage, self)._init_()

    def run(self):
        map = self._blackboard.get_value('map')
        object = self._blackboard.get_value('object')

        if self.is_in_resource(object, map) and object.get_cargo_space_left()>0:
            pillage = object.pillage()
            self._blackboard.append_values(actions=pillage)
            return True

        return False


    def is_in_resource(self, object, map):
        return map.get_cell_by_pos(object.pos).resource is not None
