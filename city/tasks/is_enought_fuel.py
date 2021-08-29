import sys
import math

from bh_trees import Task

from lux.game_constants import GAME_CONSTANTS

class IsEnoughtFuel(Task):

    def __init__(self):
        super(IsEnoughtFuel, self).__init__()


    def run(self):

        LIGHT_UPKEEP=GAME_CONSTANTS['PARAMETERS']['LIGHT_UPKEEP']

        player = self._blackboard.get_value('player')
        cities = player.cities.values()
        units = player.units

        fuel = sum([city.fuel for city in cities])
        n_tiles = player.city_tile_count
        n_carts = len([i for i in units if i.is_cart()])
        n_workers = len([i for i in units if i.is_worker()])

        needed_fuel = n_tiles * LIGHT_UPKEEP['CITY'] + \
                      n_workers * LIGHT_UPKEEP['WORKER'] + \
                      n_carts * LIGHT_UPKEEP['CART']

        return True if fuel>needed_fuel else False
