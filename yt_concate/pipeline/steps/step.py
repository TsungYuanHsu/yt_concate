from abc import ABCMeta
from abc import abstractmethod


class Step(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs, utils):
        pass


class StepException(Exception):
    pass

