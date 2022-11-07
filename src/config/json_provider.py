import json
from training.src.config.base_provider import BaseProviderClass


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
    def get(item_key=None, path=None):
        """
        Method for getting data from provider.
        :param item_key: name (key) of wanted variable [str], default 'None' means all variables
        :param path: path of file to registering data from [str], raising an error when not specified
        :return: all read data [dict] or value of specific variable [str]
        """
        json_data = JSONConfigProvider._read_config(path)
        if item_key is None:
            return json_data
        elif item_key in json_data:
            return json_data[item_key]
        else:
            raise KeyError(f"No {item_key} in given file")
