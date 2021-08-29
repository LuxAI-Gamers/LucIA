import sys
import math

from bh_trees import Task


class BuildWorker(Task):

    def __init__(self):
        super(BuildWorker, self).__init__()

    def run(self):
        object = self._blackboard.get_value('object')

        build = object.build_worker()
        if build:
            actions = self._blackboard.append_values(actions=build)
            return True

        return False
