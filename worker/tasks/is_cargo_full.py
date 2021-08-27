import sys
import math

from bh_trees import Task


class IsCargoFull(Task):

    def __init__(self):
        super(IsCargoFull, self).__init__()

    def run(self):
        object = self._blackboard.get_value('object')
        return True if object.get_cargo_space_left()==0 else False
