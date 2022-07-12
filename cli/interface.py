
from calculator import calculate


class Interface():
    """Gets the commandstring from the user and executes the cacluator"""
    # Should just loook like calculate> ...... for now

    def __init__(self):
        self.calculator = calculate.Calculator

    def startInterface(self):
        pass
