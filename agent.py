import math, sys

from lux.game import Game
from lux.game_map import Cell, RESOURCE_TYPES
from lux.constants import Constants
from lux.game_constants import GAME_CONSTANTS
from lux import annotate

from bh_trees import BlackBoard
from worker import create_dumb_worker


DIRECTIONS = Constants.DIRECTIONS
game_state = None


def agent(observation, configuration):
    global game_state

    ### Do not edit ###
    if observation["step"] == 0:
        game_state = Game()
        game_state._initialize(observation["updates"])
        game_state._update(observation["updates"][2:])
        game_state.id = observation.player

    else:
        game_state._update(observation["updates"])

    ### AI Code goes down here! ###
    bb = BlackBoard(id = game_state.id,
                    map = game_state.map,
                    turn = game_state.turn,
                    width = game_state.map_width,
                    height = game_state.map.height,                    
                    actions = [],
                    player = game_state.players[observation.player]
                    )
    
    worker = create_dumb_worker()

    for city in bb.get_value('player').cities:

        bb.set_value('object', city)

    for unit in bb.get_value('player').units:
        
        bb.set_value('object', unit)

        worker.run()

        print(bb.get_value('actions'))
    
    actions = bb.get_value('actions')
    bb.reset_memory()
    return list(set(actions))