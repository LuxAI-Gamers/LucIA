from .tasks import CanAct
from .tasks import Pillage
from .tasks import IsCargoFull
from .tasks import MoveToPosition
from .tasks import FindNearestCity
from .tasks import FindNearestResource

from bh_trees import Inverter, Sequence, Selector


def create_dumb_worker():

    root = Selector()

    # 1st level
    check_sequence = root.add_child(Sequence())
    research_sequence = root.add_child(Sequence())
    root.add_child(CreateWorker())

    # 2nd level
    check_sequence.add_child(CanAct())
    check_sequence.add_child(IsEnoughtFuel())

    inverter = research_sequence.add_child(Inverter())
    reserch_node = research_sequence.add_child(Research())

    # 3rt level
    is_researched = inverter.add_child(IsResearched())


    return root
