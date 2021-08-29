import sys
import math

from bh_trees import Task


class Research(Task):

    def __init__(self):
        super(Research, self).__init__()

    def run(self):
        object = self._blackboard.get_value('object')

        research = object.research()
        if research:
            actions = self._blackboard.append_values(actions=research)
            return True

        return False

