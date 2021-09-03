import gc
import sys
import math

from lux.game import Game
from lux.game_map import Cell, RESOURCE_TYPES
from lux.constants import Constants
from lux.game_constants import GAME_CONSTANTS
from lux import annotate

from bh_trees import BlackBoard
from worker import create_simple_worker, create_night_worker
from city import create_simple_city, create_night_city


DIRECTIONS = Constants.DIRECTIONS
game_state = None
bb = BlackBoard()

def agent(observation, configuration):
    global game_state
    global bb

    ### Do not edit ###
    if observation["step"] == 0:
        game_state = Game()
        game_state._initialize(observation["updates"])
        game_state._update(observation["updates"][2:])
        game_state.id = observation.player

    else:
        game_state._update(observation["updates"])

    ### AI Code goes down here! ###

    # Set day and night behavior
    if game_state.turn%40<=30:
        city_tree = create_simple_city()
        worker_tree = create_simple_worker()

    if game_state.turn%40>30:
        city_tree = create_night_city()
        worker_tree = create_night_worker()


    # Build units map
    player = game_state.players[observation.player]
    oponent = game_state.players[(observation.player+1)%2]


    units_map = [None] * game_state.map_height
    for y in range(0, game_state.map_height):
        units_map[y] = [None] * game_state.map_width
        for x in range(0, game_state.map_width):
            units_map[y][x] = None

    for unit in player.units + oponent.units:
        units_map[unit.pos.y][unit.pos.x] = [unit.team, unit.type]



    bb.set_values(id = game_state.id,
                  map = game_state.map,
                  units_map = units_map,
                  turn = game_state.turn,
                  width = game_state.map_width,
                  height = game_state.map.height,
                  player = game_state.players[observation.player],
                  actions = []
                  )

    # Run cities
    for city in bb.get_value('player').cities.values():
        for city_tile in city.citytiles:
            bb.set_values(object=city_tile)
            city_tree.run()

    # Run units
    for unit in bb.get_value('player').units:
        bb.set_values(object=unit)
        worker_tree.run()

    actions = bb.get_value('actions')

    return actions


if __name__=='__main__':

    import json
    from kaggle_environments import make

    env = make("lux_ai_2021",
               configuration={"seed": 562124210,
                              "loglevel": 2,
                              "annotations": True},
               debug=True)

    steps = env.run([agent, "simple_agent"])
    print([step[0]['action'] for step in steps])

#    replay = env.toJSON()
#    with open("replay.json", "w") as f:
#        json.dump(replay, f)
