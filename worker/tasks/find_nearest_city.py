import sys
import math

from bh_trees import Task


class FindNearestCity(Task):


    def __init__(self):
        super(FindNearestCity, self).__init__()


    def run(self):
        object = self._blackboard.get_value('object')
        player = self._blackboard.get_value('player')

        close_city = self.find_closest_city(player, object)
        self._blackboard.set_values(position=close_city.pos)

        return True if close_city else False


    def find_closest_city(self, player, object):

        closest_city_tile = None
        if len(player.cities) > 0:
            closest_dist = math.inf

            for k, city in player.cities.items():
                for city_tile in city.citytiles:
                    dist = city_tile.pos.distance_to(object.pos)
                    if dist < closest_dist:
                        closest_dist = dist
                        closest_city_tile = city_tile

        return closest_city_tile
