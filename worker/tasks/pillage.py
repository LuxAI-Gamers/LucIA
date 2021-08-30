from bh_trees import Task


class Pillage(Task):


    def __init__(self):
        super(Pillage, self).__init__()

    def run(self):
        object = self._blackboard.get_value('object')

        pillage = object.pillage()
        if pillage:
            actions = self._blackboard.append_values(actions=pillage)
            return True

        return False
