import math, sys

from lux.game import Game
from lux.game_map import Cell, RESOURCE_TYPES
from lux.constants import Constants
from lux.game_constants import GAME_CONSTANTS
from lux import annotate

from worker_tasks.behaviour_trees import *


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
    blackboard = Blackboard(id = game_state.id,
                            map = game_state.map,
                            turn = game_state.turn,
                            width = game_state.map_width,
                            height = game_state.map.height,
                            player = game_state.players[observation.player],
                            opponent = game_state.players[(observation.player+1)%2],
                            actions = []
                            )

    return blackboard.get_value('actions')