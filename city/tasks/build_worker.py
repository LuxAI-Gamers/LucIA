import sys
import math

from lux.game_constants import GAME_CONSTANTS

from bh_trees import Task


class BuildWorker(Task):

    def __init__(self):
        super(BuildWorker, self).__init__()

    def run(self):
        object = self._blackboard.get_value('object')
        player = self._blackboard.get_value('player')

        # Condition to build worker
        n_units = len(player.units)
        n_tiles = player.city_tile_count
        if n_tiles>n_units:
            build = object.build_worker()
            self._blackboard.append_values(actions=build)
            return True

        return False
