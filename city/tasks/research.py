import sys
import math

from bh_trees import Task


class Research(Task):

    def __init__(self):
        super(Research, self).__init__()

    def run(self):
        object = self._blackboard.get_value('object')
        return True if object.research() else False
