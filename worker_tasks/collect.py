import sys
import math

from behaviour_trees import Task


class Pillage(Task):


    def __init__(self):
        super(Pillage, self).__init__()

    def run(self):
        unit = self._blackboard.get_value('unit')
        return True if unit.pillage() else False