from .tasks import CanAct
from .tasks import Pillage
from .tasks import IsCargoFull
from .tasks import MoveToPosition
from .tasks import FindNearestCity
from .tasks import FindNearestResource

from bh_trees import recursive_build
from bh_trees import Inverter, Sequence, Selector


def create_dumb_worker():

    graph = {
        Selector(): {
            Inverter(): {
                CanAct(): {}
                },
            Sequence(): {
                IsCargoFull(): {},
#                Sequence(): {
#                   CanBuildCityTile(): {},
#                   BuildCityTile(): {}
#                    },
                FindNearestCity(): {},
                MoveToPosition(): {}
               },
            Sequence(): {
                FindNearestResource(): {},
                Selector(): {
                    MoveToPosition(): {},
                    Pillage(): {}
                    }
                }
            }
        }

    return recursive_build(graph)
