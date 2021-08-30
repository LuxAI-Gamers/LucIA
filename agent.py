import gc
import sys
import math

from lux.game import Game
from lux.game_map import Cell, RESOURCE_TYPES
from lux.constants import Constants
from lux.game_constants import GAME_CONSTANTS
from lux import annotate

from bh_trees import BlackBoard
from worker import create_simple_worker
from city import create_simple_city


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
    bb.set_values(id = game_state.id,
                  map = game_state.map,
                  turn = game_state.turn,
                  width = game_state.map_width,
                  height = game_state.map.height,
                  player = game_state.players[observation.player],
                  actions = []
                  )

    city_tree = create_simple_city()
    worker_tree = create_simple_worker()


    for city in bb.get_value('player').cities.values():
        for city_tile in city.citytiles:
            bb.set_values(object=city_tile)
            city_tree.run()

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
