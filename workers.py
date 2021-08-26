from worker_tasks.pillage import Pillage
from worker_tasks.behaviour_trees import Inverter, Sequence, Selector
from worker_tasks.can_act import CanAct
from worker_tasks.is_cargo_full import CargoFull
from worker_tasks.find_nearest_city import FindNearestCity
from worker_tasks.find_nearest_resource import FindNearestResource
from worker_tasks.move_to_position import MoveToPosition
from worker_tasks.pillage import Pillage


def dumb_worker():


    tree = Selector()

    # 1st level
    first = root.add_child(Inverter())
    back_to_city_seq = root.add_child(Sequence())
    collect_seq = root.add_child(Sequence())

    # 2nd level
    first.add_child(CanAct())
    back_to_city_seq.add_child(CargoFull())
    back_to_city_seq.add_child(FindNearestCity())
    back_to_city_seq.add_child(MoveToPosition())
    collect_seq.add_child(FindNearestResource())
    collect_seq = collect_seq.add_child(Selector())

    # 3rd level
    collect_seq.add_child(Pillage())
    collect_seq.add_child(MoveToPosition())

    return tree