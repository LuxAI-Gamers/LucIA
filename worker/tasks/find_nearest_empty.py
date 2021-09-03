import math
import random

from lux.constants import Constants

from bh_trees import Task


class FindNearestEmpty(Task):

    DIRECTIONS = [
            Constants.DIRECTIONS.NORTH,
            Constants.DIRECTIONS.EAST,
            Constants.DIRECTIONS.SOUTH,
            Constants.DIRECTIONS.WEST,
        ]

    def __init__(self):
        super(FindNearestEmpty, self).__init__()


    def run(self):
        object = self._blackboard.get_value('object')
        player = self._blackboard.get_value('player')
        game_map = self._blackboard.get_value('map')
        width = self._blackboard.get_value('width')
        height = self._blackboard.get_value('height')

#        close_city = self.find_closest_city(player, object)

        random.shuffle(self.DIRECTIONS)
        for dir in self.DIRECTIONS:
            pos = object.pos.translate(dir,1)
            if pos.x>=0 and pos.y>=0 and pos.x<width and pos.y<height:
                cell = game_map.get_cell_by_pos(pos)
                if cell.resource is None and cell.citytile is None:
                    if pos:
                        self._blackboard.set_values(position = pos)
                        return True

        return False


#    def find_closest_city(self, player, object):

#        closest_city_tile = None
#        if len(player.cities) > 0:
#            closest_dist = math.inf

#            for k, city in player.cities.items():
#                for city_tile in city.citytiles:
#                    dist = city_tile.pos.distance_to(object.pos)
#                    if dist < closest_dist:
#                        closest_dist = dist
#                        closest_city_tile = city_tile

#        return closest_city_tile
