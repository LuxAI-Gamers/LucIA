from .tasks import CanAct
from .tasks import Pillage
from .tasks import IsCargoFull
from .tasks import MoveToPosition
from .tasks import FindNearestCity
from .tasks import FindNearestResource
from .tasks import CanBuildCityTile
from .tasks import BuildCityTile

from bh_trees import recursive_build
from bh_trees import Inverter, Sequence, Selector

def create_simple_worker():

    graph = {
        Selector(): {
            Inverter(): {
                CanAct(): {}
                },
            Sequence(): {
                IsCargoFull(): {},
                FindNearestCity(): {},
                Selector(): {
                    Sequence(): {
                        CanBuildCityTile(): {},
                        BuildCityTile(): {}
                        },
                    MoveToPosition(): {}
                    }
               },
            Selector(): {
                Pillage(): {}
                Sequence(): {
                    FindNearestResource(): {},
                    MoveToPosition(): {}
                    }
                }
            }
        }

    return recursive_build(graph)
