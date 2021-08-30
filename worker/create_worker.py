from .tasks import CanAct
from .tasks import Pillage
from .tasks import IsCargoFull
from .tasks import MoveToPosition
from .tasks import FindNearestCity
from .tasks import FindNearestResource
from .tasks import CanBuildCityTile
from .tasks import BuildCityTile

from bh_trees import Inverter, Sequence, Selector

def create_simple_worker():

    root = Selector()

    # 1st level
    first = root.add_child(Inverter())
    back_to_city_seq = root.add_child(Sequence())
    collect_seq = root.add_child(Sequence())

    # 2nd level
    first.add_child(CanAct())

    back_to_city_seq.add_child(IsCargoFull())
    back_to_city_seq.add_child(FindNearestCity())
    select_action = back_to_city_seq.add_child(Selector())

    collect_seq.add_child(FindNearestResource())
    collect_sel = collect_seq.add_child(Selector())


    # 3rd level
    build_city_seq = select_action.add_child(Sequence())
    select_action.add_child(MoveToPosition())

    collect_sel.add_child(MoveToPosition())
    collect_sel.add_child(Pillage())

    # 4th level
    build_city_seq.add_child(CanBuildCityTile())
    build_city_seq.add_child(BuildCityTile())

    return root
