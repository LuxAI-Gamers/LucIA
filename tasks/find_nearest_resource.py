import sys
import math

from lux.game import Game
from lux.game_map import Cell, RESOURCE_TYPES
from lux.constants import Constants
from lux.game_constants import GAME_CONSTANTS
from lux import annotate

from behaviour_tree import Task


class FindNearestResource(Task):

    def __init__(self):
        super(FindNearestCity, self).__init__()


    def run(self):
        """
        """
        unit = self.blackboard.get_value('unit')
        player = self.blackboard.get_value('player')
        game_state = self.blackboard.get_value('game_state')

        tiles_resource = self.find_all_resources(game_state)
        close_resource = self.find_closest_resource(unit, player, tiles)

        self.blackboard.set_value('nearest_resource',close_resource)

        return True if close_resource else False


    def find_all_resources(self,game_state):
        """
        """
        resource_tiles = []
        for y in range(game_state.map_height):
            for x in range(game_state.map_width):
                cell = game_state.map.get_cell(x, y)
                if cell.has_resource():
                    resource_tiles.append(cell)

        self._resource_tiles = resource_tiles


    def find_closest_resources(self, unit, player):
        """
        """
        closest_dist = math.inf
        closest_resource_tile = None
        for resource_tile in self._resource_tiles:

            if (resource_tile.resource.type == Constants.RESOURCE_TYPES.COAL
                and not player.researched_coal()):
                continue

            if (resource_tile.resource.type == Constants.RESOURCE_TYPES.URANIUM
                and not player.researched_uranium()):
                continue

            dist = resource_tile.pos.distance_to(unit.pos)
            if dist < closest_dist:
                closest_dist = dist
                closest_resource_tile = resource_tile

        return closest_resource_tile
