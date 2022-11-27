import os
import logging
from src.providers.data.base_provider import BaseProviderClass

log = logging.getLogger()


class OSConfigProvider(BaseProviderClass):
    """
    Class for getting environment variables from operating system.
    """

    @staticmethod
    def get(item_key='all', path=None):
        """
        Method for getting data from provider.
        :param item_key: name (key) of wanted variable [str], default 'None' means all variables
        :param path: always default, that is parameter for another class
        :return: all environment variables [dict] or value of specific variable [str]
        """
        if item_key == 'all':
            return os.environ
        elif item_key in os.environ:
            return os.getenv(item_key)
        else:
            log.info(f"Can not register {item_key} - no item in environment variables")

    def __str__(self):
        return 'OS config provider'
