import sys
import math

from bh_trees import Task


class CanAct(Task):

    def __init__(self):
        super(CanAct, self).__init__()

    def run(self):
        object = self._blackboard.get_value('object')
        return True if object.can_act() else False
