import sys
import math

from .behaviour_trees import Task


class CargoFull(Task):

    def __init__(self):
        super(CargoFull, self).__init__()

    def run(self):
        unit = self._blackboard.get_value('unit')
        return True if unit.get_cargo_space_left()==0 else False
