from .tasks import CanAct
from .tasks import Research
from .tasks import BuildWorker
from .tasks import IsEnoughtFuel
from .tasks import CanBuildWorker
from .tasks import IsResourceResearched

from bh_trees import recursive_build
from bh_trees import Inverter, Sequence, Selector


def create_simple_city():

    graph = {
        Sequence(): {
            Sequence(): {
                CanAct(): {},
                IsEnoughtFuel(): {}
                },
            Selector(): {
                Sequence(): {
                    Inverter(): {
                        IsResourceResearched(): {}
                        },
                    Research(): {}
                    },
                Sequence(): {
                    BuildWorker(): {},
                    CanBuildWorker(): {}
                    }
                }
            }
        }

    return recursive_build(graph)
