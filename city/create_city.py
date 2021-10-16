from .tasks import CanAct
from .tasks import Research
from .tasks import BuildWorker
from .tasks import IsEnoughtFuel
from .tasks import IsResourceResearched

from bh_trees import recursive_build
from bh_trees import Inverter, Sequence, Selector


def create_day_city():

    graph = {
        Sequence(): {
            Sequence(): {
                CanAct(): {},
                IsEnoughtFuel(): {}
                },
            Selector(): {
                BuildWorker(): {},
                Sequence(): {
                    Inverter(): {
                        IsResourceResearched(): {}
                        },
                    Research(): {}
                    }
                }
            }
        }

    return recursive_build(graph)


def create_night_city():

    graph = {
        Sequence():{}
        }

    return recursive_build(graph)
