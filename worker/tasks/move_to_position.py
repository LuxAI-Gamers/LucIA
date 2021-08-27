import sys
import math

from bh_trees import Task
from lux.constants import Constants


class MoveToPosition(Task):

    def __init__(self):
        super(MoveToPosition, self).__init__()

    def run(self):
        object = self._blackboard.get_value('object')
        position = self._blackboard.get_value('position')
        direction = object.pos.direction_to(position)
        movement = object.move(direction)

        # If object in the position of interest then don't move
        if direction != Constants.DIRECTIONS.CENTER:
            actions = self._blackboard.append_values(actions=movement)
            return True
        else:
            return False
