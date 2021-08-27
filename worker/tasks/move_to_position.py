import sys
import math

from bh_trees import Task
from lux import constants


class MoveToPosition(Task):

    def __init__(self):
        super(MoveToPosition, self).__init__()

    def run(self):
        object = self._blackboard.get_value('object')
        position = self._blackboard.get_value('position')
        direction = object.pos.direction_to(position)
        movement = object.move(direction)

        # If object in the position of interest then don't move
        if direction != constants.DIRECTIONS.CENTER:
            actions = self._blackboard.get_value('actions')
            actions.append(movement)
            self._blackboard.set_value('actions', actions)
            print('MOVE TO POSITION: ', movement)
            return True
        else:
            return False
