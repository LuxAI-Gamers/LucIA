import sys
import math

from bh_trees import Task

from lux.game_constants import GAME_CONSTANTS

class CanBuildWorker(Task):

    def __init__(self):
        super(CanBuildWorker, self).__init__()


    def run(self):

        player = self._blackboard.get_value('player')

        n_units = len(player.units)
        n_tiles = player.city_tile_count

        return True if n_tiles>n_units else False
