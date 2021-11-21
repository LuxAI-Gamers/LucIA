from ...bh_trees import Task


class BuildCityTile(Task):

    def __init__(self):
        super (BuildCityTile, self).__init__()

    def run(self):
        object = self._blackboard.get_value('object')
        game_map = self._blackboard.get_value('map')

        # Condition if it can build
        if object.can_build(game_map):
            build = object.build_city()
            self._blackboard.append_values(actions=build)
            return True
        return False

