import sys
import math

from behaviour_trees import Task


class FindNearestCity(Task):


    def __init__(self):
        super(FindNearestCity, self).__init__()


    def run(self):
        unit = self._blackboard.get_value('unit')
        player = self._blackboard.get_value('player')

        close_city = self.find_closest_city(player, unit)
        self._blackboard.set('position', close_city)

        return True if close_city else False


    def find_closest_city(self, player, unit):

        closest_city_tile = None
        if len(player.cities) > 0:
            closest_dist = math.inf

            for k, city in player.cities.items():
                for city_tile in city.citytiles:
                    dist = city_tile.pos.distance_to(unit.pos)
                    if dist < closest_dist:
                        closest_dist = dist
                        closest_city_tile = city_tile

        return closest_city_tile
