import sys
import math

from behaviour_tree import Task


class CanAct(Task):

    def __init__(self):
        super(CanAct, self).__init__()

    def run(self):
        unit = self.blackboard.get_value('unit')
        return True if unit.can_act() else False
