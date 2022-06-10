from abc import ABCMeta, abstractmethod


class PaginationCommand:
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def next_page_url():
        pass
