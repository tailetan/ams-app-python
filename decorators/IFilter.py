from abc import ABCMeta, abstractmethod


class IFilter:
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def filter(self):
        pass
