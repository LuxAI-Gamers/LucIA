import threading

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BlackBoard(metaclass=Singleton):
    """
    """
    def __init__(self,**kwargs):
        self._memory = {}

    def set_values(self, **kwargs):
        for key,val in kwargs.items():
            self._memory[key] = val

    def get_value(self, key):
        return self._memory[key]

    def reset_memory(self):
        self._memory = {}

    def append_values(self, **kwargs):
        for key,val in kwargs.items():
            self._memory[key].append(val)
