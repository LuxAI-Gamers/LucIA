def recursive_build(tree_graph):
    for parent, children in tree_graph.items():
        for child, grandson in children.items():
            parent.add_child(child)
            recursive_build({child: grandson})
    return parent


if __name__=='__main__':

    tree_graph={
        Selector(): {
            Inverter(): {
                CanAct(): {}
                },
            Sequence(): {
                FindNearestCity(): {},
                IsCargoFull(): {},
                MoveToPosition(): {}
                },
            Sequence(): {
                BuildCityTile(): {},
                CanBuildCityTile(): {}},
            Sequence(): {
                FindNearestResource(): {},
                Selector(): {
                    MoveToPosition(): {},
                    Pillage(): {}
                    }
                }
            }
        }


    bh_tree = recursive_build(tree_graph)
