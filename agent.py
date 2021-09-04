from lux.game import Game
from lux.game_map import Cell, RESOURCE_TYPES
from lux.constants import Constants
from lux.game_constants import GAME_CONSTANTS
from lux import annotate

from lucia import LucIA

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
    actions = LucIA().play(game_state, observation)

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

    replay = env.toJSON()
    with open("replay.json", "w") as f:
        json.dump(replay, f)
