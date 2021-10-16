from .tasks import CanAct
from .tasks import Pillage
from .tasks import IsCargoFull
from .tasks import IsCityNeeded
from .tasks import MoveToPosition
from .tasks import FindNearestCity
from .tasks import FindNearestEmpty
from .tasks import FindNearestResource
from .tasks import BuildCityTile

from bh_trees import recursive_build
from bh_trees import Inverter, Sequence, Selector


def create_day_worker():

    graph = {
        Sequence(): {
            CanAct(): {},
            Selector(): {
                Sequence(): {
                    IsCargoFull(): {},
                    IsCityNeeded(): {},
                    FindNearestEmpty(): {}
                    },
                Sequence(): {
                    IsCargoFull(): {},
                    FindNearestCity(): {}
                    },
                FindNearestResource(): {}
                },
            Selector(): {
                Sequence(): {
                    IsCargoFull(): {},
                    BuildCityTile(): {}
                    },
                Pillage(): {},
                MoveToPosition(): {}
                }
            }
        }

    return recursive_build(graph)


def create_night_worker():

    graph = {
        Sequence(): {
            CanAct(): {},
            Selector(): {
                Sequence(): {
                    IsCargoFull(): {},
                    FindNearestCity(): {},
                    },
                FindNearestResource(): {}
                },
            Selector(): {
                Pillage(): {},
                MoveToPosition(): {}
                }
            }
        }

    return recursive_build(graph)
