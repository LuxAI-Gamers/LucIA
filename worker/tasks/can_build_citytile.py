import sys
import math

from bh_trees import Task


class CanBuildCityTile(Task):

    def __init__(self):
        super(CanBuildCityTile, self).__init__()

    def run(self):
        object = self._blackboard.get_value('object')
        return True if object.can_build() else False
