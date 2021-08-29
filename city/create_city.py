from .tasks import CanAct
from .tasks import Research
from .tasks import CreateWorker
from .tasks import IsEnoughtFuel
from .tasks import IsResourceResearched

from bh_trees import Inverter, Sequence, Selector


def create_simple_city():

    root = Sequence()

    # 1st level
    check_sequence = root.add_child(Sequence())
    action_selector = root.add_child(Selector())

    # 2nd level
    check_sequence.add_child(CanAct())
    check_sequence.add_child(IsEnoughtFuel())

    research_sequence = action_selector.add_child(Sequence())
    action_selector.add_child(CreateWorker())

    # 3rd level
    not_researched = research_sequence.add_child(Inverter())
    reserch_node = research_sequence.add_child(Research())

    # 4th level
    is_researched = not_researched.add_child(IsResourceResearched())

    return root
