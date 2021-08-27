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

        for key,val in kwargs.items():
            if key not in self._memory:
                self._memory[key] = val

    def set_value(self, key, val):
        self._memory[key] = val

    def get_value(self, key):
        return self._memory[key]

    def reset_memory(self):
        self._memory = {}

    def append_value(self, key, val):
        self._memory[key].append(val)



class Task:
    """
    """
    def __init__(self):
        self._children = []
        self._blackboard = BlackBoard()

    def add_child(self, child):
        self._children.append(child)
        return child

    def print(self):

        name = self.__class__.__name__

        children = {}
        for index, child in enumerate(self._children):
            for key, val in child.print().items():
                children[f'{key}_{index}'] = val

        return {name: children}


class Selector(Task):
    """
    """
    def __init__(self):
        super(Selector, self).__init__()

    def run(self):
        for c in self._children:
            if c.run():
                return True
        return False


class Sequence(Task):
    """
    """
    def __init__(self):
        super(Sequence, self).__init__()

    def run(self):
        for c in self._children:
            if not c.run():
                return False
        return True


class Inverter(Task):
    """
    """
    def __init__(self):
        super(Inverter, self).__init__()

    def run(self):
        if len(self._children) > 1:
            raise Exception('Inverter node has more than 1 children')

        c = self._children[0]
        return not c.run()
