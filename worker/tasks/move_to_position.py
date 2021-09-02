from bh_trees import Task
from lux.constants import Constants


class MoveToPosition(Task):

    DIRECTIONS = [
            Constants.DIRECTIONS.NORTH,
            Constants.DIRECTIONS.EAST,
            Constants.DIRECTIONS.SOUTH,
            Constants.DIRECTIONS.WEST,
        ]

    def __init__(self):
        super(MoveToPosition, self).__init__()


    def run(self):

        object = self._blackboard.get_value('object')
        source_position = self._blackboard.get_value('object').pos
        target_position = self._blackboard.get_value('position')


        closest_distance = self.get_closest_dist(source_position,
                                                 target_position)

        posible_positions = self.get_posible_positions(source_position,
                                                       target_position,
                                                       closest_distance)

        direction = self.get_final_position(posible_positions,
                                                    object)
        updated = self.update_blackboard(direction,
                                         object)

        return True if updated else False


    def get_closest_dist(self,source_position,target_position):

        closest_dis = source_position.distance_to(target_position)

        for dir in self.DIRECTIONS:
            new_pos = source_position.translate(dir, 1)
            new_dis = target_position.distance_to(new_pos)

            if new_dis < closest_dis:
                closest_dis = new_dis

        return closest_dis


    def get_posible_positions(self,source_position,
                                   target_position,
                                   closest_distance):

        posible_pos = []
        for dir in self.DIRECTIONS:
            new_pos = source_position.translate(dir, 1)
            new_dis = target_position.distance_to(new_pos)

            if new_dis == closest_distance:
                posible_pos.insert(0,new_pos)
            else:
                posible_pos.insert(-1,new_pos)

        return posible_pos


    def get_final_position(self,posible_pos,object):

        units_map = self._blackboard.get_value('units_map')

        direction = None
        for pos in posible_pos:
            if units_map[pos.y][pos.x] is None:
                direction = object.pos.direction_to(pos)
                break

        return direction


    def update_blackboard(self, direction, object):

        if direction:
            old_pos = object.pos
            new_pos = object.pos.translate(direction,1)
            movement  = object.move(direction)

            units_map = self._blackboard.get_value('units_map')
            units_map[new_pos.y][new_pos.x] = 1
            units_map[old_pos.y][old_pos.y] = None

            self._blackboard.set_values(units_map=units_map)
            self._blackboard.append_values(actions=movement)
            return True
        else:
            return False
