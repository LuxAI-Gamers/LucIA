import sys
import math

from bh_trees import Task


class CreateWorker(Task):

    def __init__(self):
        super(CreateWorker, self).__init__()

    def run(self):
        object = self._blackboard.get_value('object')
        return True if object.build_worker() else False
