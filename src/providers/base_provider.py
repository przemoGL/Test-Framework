class BaseProviderClass:
    """
    Parent class for config providers.
    It raises an error when child class has no implemented get method.
    """

    @staticmethod
    def get(item_key='all', path=None):
        """
        Method for getting data from config provider.
        :param item_key: always default, that is parameter for another class
        :param path: always default, that is parameter for another class
        :return: error (when child class has no implemented get method)
        """
        raise NotImplementedError("Class with no get method")
