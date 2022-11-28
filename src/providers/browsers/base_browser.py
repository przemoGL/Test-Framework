from abc import ABC, abstractmethod


class BaseBrowser(ABC):

    @abstractmethod
    def get_driver(self):
        pass
