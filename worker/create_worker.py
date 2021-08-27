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
    first = root.add_child(Inverter())
    back_to_city_seq = root.add_child(Sequence())
    collect_seq = root.add_child(Sequence())

    # 2nd level
    first.add_child(CanAct())
    back_to_city_seq.add_child(IsCargoFull())
    back_to_city_seq.add_child(FindNearestCity())
    back_to_city_seq.add_child(MoveToPosition())
    collect_seq.add_child(FindNearestResource())
    collect_seq = collect_seq.add_child(Selector())

    # 3rd level
    collect_seq.add_child(Pillage())
    collect_seq.add_child(MoveToPosition())

    return root
