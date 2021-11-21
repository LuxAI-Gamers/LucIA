from .bh_trees import BlackBoard
from .city import create_simple_city
from .city import create_night_city
from .worker import create_simple_worker
from .worker import create_night_worker


class LucIA():

    """
    Hi! I am LucIA, an IA based in Behavioural Trees
    """

    def __init__(self):

        """
        Open my notebook to annotate the movements
        """

        self.notes = BlackBoard()


    def play(self, game_state, observation):

        """
        TIME TO PLAY!!!!
        """

        self._init_my_turn(game_state, observation)
        self._choose_strategy()
        self._see_gameboard()
        self._write_notes()
        self._move_pieces()

        return self.notes.get_value('actions')


    def _init_my_turn(self, game_state, observation):

        """
        Ok! Let's see how are we going
        """

        self._id = game_state.id
        self._map = game_state.map
        self._turn = game_state.turn
        self._width = game_state.map_width
        self._height = game_state.map.height
        self._player = game_state.players[observation.player]
        self._opponent = game_state.players[(observation.player+1)%2]
        self._n_units = len(game_state.players[observation.player].units)


    def _move_pieces(self):

        """
        YES! With my strategy the best movements are clear!!
        """

        # Run cities
        for city in self._player.cities.values():
            for city_tile in city.citytiles:
                self.notes.set_values(object=city_tile)
                self._city_tree.run()

        # Run units
        for unit in self._player.units:
            self.notes.set_values(object=unit)
            self._worker_tree.run()


    def _choose_strategy(self):

        """
        Mmmmm... What should I do?
        """

        # Choose day behavior
        if self._turn%40<=30:
            self._city_tree = create_simple_city()
            self._worker_tree = create_simple_worker()

        # Choose night behavior
        if self._turn%40>30:
            self._city_tree = create_night_city()
            self._worker_tree = create_night_worker()


    def _see_gameboard(self):

        """
        Take a time to see the pieces distribution
        """

        # Create empty map
        units_map = [None] * self._height
        for y in range(0, self._height):
            units_map[y] = [None] * self._width
            for x in range(0, self._width):
                units_map[y][x] = None

        # Mark units in map
        for unit in self._player.units + self._opponent.units:
            units_map[unit.pos.y][unit.pos.x] = [unit.team, unit.type]

        # Mark opponen cities in map
        for city in self._opponent.cities.values():
            for city_tile in city.citytiles:
                units_map[city_tile.pos.y][city_tile.pos.x] = [city_tile.team]

        self._units_map = units_map


    def _write_notes(self):

        """
        I need to remember this. I have to annotate it.
        """

        self.notes.set_values(actions = [],
                              id = self._id,
                              map = self._map,
                              turn = self._turn,
                              width = self._width,
                              height = self._height,
                              player = self._player,
                              n_units = self._n_units,
                              units_map = self._units_map,
                              tiles_assigned = []
                              )
