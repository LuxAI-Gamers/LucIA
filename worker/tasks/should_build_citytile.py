from bh_trees import Task


class CanBuildCityTile(Task):

    def __init__(self):
        super(CanBuildCityTile, self).__init__()

    def run(self):
        # Number of cities equal to number of workers

        # Reduce city cost

        # City near resource


        object = self._blackboard.get_value('object')
        game_map = self._blackboard.get_value('map')
        return True if object.can_build(game_map) else False
