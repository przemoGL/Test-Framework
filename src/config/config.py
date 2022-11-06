import os
import json


class BaseProviderClass:
    """
    Parent class for config providers.
    It raises an error when child class has no implemented get method.
    """

    @staticmethod
    def get(item_key=None, path=None):
        """
        Method for getting data from config provider.
        :param item_key: always default, that is parameter for another class
        :param path: always default, that is parameter for another class
        :return: error (when child class has no implemented get method)
        """
        raise NotImplementedError("Class with no get method")


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


class Config:
    """
    Holds all the settings of framework.
    """

    def __init__(self, config_providers: list):
        """
        Method to initializing providers and creating empty container for settings [dict].
        :param config_providers: instances of wanted providers [list]
        """
        self.config_providers = config_providers
        self.configs = {}

    def register(self, item_key=None, path=None):
        """
        Method to registering wanted data to configs [dict] from providers.
        :param item_key: name (key) of wanted variable [str], default 'None' means all variables
        :param path: path of file to registering data from [str], default 'None' means provider do not require file
        :return: registered data [str]
        """
        for provider in self.config_providers:
            # get all data from provider
            if item_key is None:
                self.configs = self.configs | provider.get(item_key, path)
                self.set_attributes()
                return f'Registered all variables: {self.configs}'
            # get specific data from OS provider
            elif path is None and isinstance(provider, OSConfigProvider):
                item_value = provider.get(item_key, path)
                if item_value is not None:
                    self.configs[item_key] = item_value
                    self.set_attributes()
                    return f'Registered: {item_key} -> {item_value}'
            # get specific data from JSON provider
            elif path is not None and isinstance(provider, JSONConfigProvider):
                item_value = provider.get(item_key, path)
                if item_value is not None:
                    self.configs[item_key] = item_value
                    self.set_attributes()
                    return f'Registered: {item_key} -> {item_value}'
            # elif not (path is None and isinstance(provider, JSONConfigProvider))
        raise ValueError(f"There is no {item_key} in config providers")

    def set_attributes(self):
        """
        Method to set registered data records as instance attributes.
        """
        for item_key, item_value in self.configs.items():
            setattr(self, item_key, item_value)


print('-------------------------------------------------------------------------------------')
# Register all variables from OS provider
config_1 = Config([OSConfigProvider()])
print(config_1.register())
print(f'TEMP -> {config_1.TEMP}\n')

print('-------------------------------------------------------------------------------------')
# Register all variables from JSON provider
config_2 = Config([JSONConfigProvider()])
print(config_2.register(path='../../envs_config/dev.json'))
print(f'SQL_CONNECTION_STRING -> {config_2.SQL_CONNECTION_STRING}\n')

print('-------------------------------------------------------------------------------------')
# Register selected variables from OS and JSON providers
config_3 = Config([OSConfigProvider(), JSONConfigProvider()])
print(config_3.register("TEMP"))
print(config_3.register("SQL_CONNECTION_STRING", path='../../envs_config/dev.json'))
print()
print(f'TEMP -> {config_3.TEMP}')
print(f'SQL_CONNECTION_STRING -> {config_3.SQL_CONNECTION_STRING}')
print('-------------------------------------------------------------------------------------')
