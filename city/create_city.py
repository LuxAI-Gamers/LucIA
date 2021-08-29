from .tasks import CanAct
from .tasks import Research
from .tasks import CreateWorker
from .tasks import IsEnoughtFuel
from .tasks import IsResourceResearched

from bh_trees import Inverter, Sequence, Selector


def create_simple_city():

    root = Selector()

    # 1st level
    check_sequence = root.add_child(Sequence())
    research_sequence = root.add_child(Sequence())
    root.add_child(CreateWorker())

    # 2nd level
    not_can_act = check_sequence.add_child(Inverter())
    not_enought_fuel = check_sequence.add_child(Inverter())

    inverter = research_sequence.add_child(Inverter())
    reserch_node = research_sequence.add_child(Research())

    # 3rt level
    not_can_act.add_child(CanAct())
    not_enought_fuel.add_child(IsEnoughtFuel())
    is_researched = inverter.add_child(IsResourceResearched())

    return root
