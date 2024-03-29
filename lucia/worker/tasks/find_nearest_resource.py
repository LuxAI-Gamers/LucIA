import math

from lux.constants import Constants
from ...bh_trees import Task


class FindNearestResource(Task):

    def __init__(self):
        super(FindNearestResource, self).__init__()


    def run(self):
        """
        """
        map = self._blackboard.get_value('map')
        object = self._blackboard.get_value('object')
        width = self._blackboard.get_value('width')
        height = self._blackboard.get_value('height')
        player = self._blackboard.get_value('player')

        tiles_resource = self.find_all_resources(map, width, height)
        close_resource = self.find_closest_resources(object, player)

        if close_resource:
            self._blackboard.set_values(position=close_resource.pos)
            return True

        return False


    def find_all_resources(self, map, height, width):
        """
        """
        resource_tiles = []
        for y in range(height):
            for x in range(width):
                cell = map.get_cell(x, y)
                if cell.has_resource():
                    resource_tiles.append(cell)

        self._resource_tiles = resource_tiles


    def find_closest_resources(self, object, player):
        """
        """

        tiles_assigned = self._blackboard.get_value('tiles_assigned')

        closest_dist = math.inf
        closest_resource_tile = None
        for resource_tile in self._resource_tiles:

            if (resource_tile.resource.type == Constants.RESOURCE_TYPES.COAL
                and not player.researched_coal()):
                continue

            if (resource_tile.resource.type == Constants.RESOURCE_TYPES.URANIUM
                and not player.researched_uranium()):
                continue

            if resource_tile.pos in tiles_assigned:
                continue

            dist = resource_tile.pos.distance_to(object.pos)
            if dist < closest_dist:
                closest_dist = dist
                closest_resource_tile = resource_tile

        return closest_resource_tile
