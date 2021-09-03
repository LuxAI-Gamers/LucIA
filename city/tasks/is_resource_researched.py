from bh_trees import Task


class IsResourceResearched(Task):

    def __init__(self):
        super(IsResourceResearched, self).__init__()

    def run(self):
        player = self._blackboard.get_value('player')
        return player.researched_uranium()
