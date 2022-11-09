import json
from src.providers.base_provider import BaseProviderClass


class JSONConfigProvider(BaseProviderClass):
    """
    Class for getting settings from specific JSON file.
    """

    @staticmethod
    def _read_config(path):
        """
        Assistance method to read JSON type file.
        :param path: path to wanted JSON file with data [str]
        :return: data from the file [dict]
        """
        if path is None:
            raise ValueError("Please specify path to JSON config file")
        with open(path) as json_file:
            return json.load(json_file)

    @staticmethod
    def get(item_key='all', json_path=None):
        """
        Method for getting data from provider.
        :param item_key: name (key) of wanted variable [str], default 'None' means all variables
        :param json_path: path of file to registering data from [str], raising an error when not specified
        :return: all read data [dict] or value of specific variable [str]
        """
        json_data = JSONConfigProvider._read_config(json_path)
        if item_key == 'all':
            return json_data
        elif item_key in json_data:
            return json_data[item_key]
        else:
            raise KeyError(f"No {item_key} in given file")

    def __str__(self):
        return 'JSON config provider'
