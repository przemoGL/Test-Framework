import os
from training.src.config.base_provider import BaseProviderClass


class OSConfigProvider(BaseProviderClass):
    """
    Class for getting environment variables from operating system.
    """

    @staticmethod
    def get(item_key=None, path=None):
        """
        Method for getting data from provider.
        :param item_key: name (key) of wanted variable [str], default 'None' means all variables
        :param path: always default, that is parameter for another class
        :return: all environment variables [dict] or value of specific variable [str]
        """
        if item_key is None:
            return os.environ
        elif item_key in os.environ:
            return os.getenv(item_key)
        else:
            raise KeyError(f"No {item_key} in environment variables")
