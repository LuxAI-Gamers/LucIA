import sys
import math

from bh_trees import Task


class BuildCityTile(Task):

    def __init__(self):
        super (BuildCityTile, self).__init__()

    def run(self):
        object = self._blackboard.get_value('object')

        build = object.build_city()
        if build:
            actions = self._blackboard.append_values(actions=build)
            return True
        return False
        