from .blackboard import BlackBoard

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
