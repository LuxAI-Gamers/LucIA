from bh_trees import Task


class IsCityNeeded(Task):

    def __init__(self):
        super(IsCityNeeded, self).__init__()

    def run(self):
        player = self._blackboard.get_value('player')
        n_units = self._blackboard.get_value('n_units')
        n_tiles = player.city_tile_count

        return True if n_units>=n_tiles else False
