from abc import ABCMeta, abstractmethod


class CRUDCommand:
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def get_list():
        pass

    @staticmethod
    @abstractmethod
    def create():
        pass
