from models.User import User
from abc import ABCMeta, abstractmethod


class CRUD:
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def create():
        pass
