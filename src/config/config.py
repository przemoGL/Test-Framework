from os_provider import OSConfigProvider
from json_provider import JSONConfigProvider


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
            # get specific data from OS or JSON provider
            elif (path is None and isinstance(provider, OSConfigProvider)) or \
                 (path is not None and isinstance(provider, JSONConfigProvider)):
                item_value = provider.get(item_key, path)
                if item_value is not None:
                    self.configs[item_key] = item_value
                    self.set_attributes()
                    return f'Registered: {item_key} -> {item_value}'
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
print(f'TEMP -> {config_1.TEMP}\n')     # test

print('-------------------------------------------------------------------------------------')
# Register all variables from JSON provider
config_2 = Config([JSONConfigProvider()])
print(config_2.register(path='../../envs_config/dev.json'))
print(f'SQL_CONNECTION_STRING -> {config_2.SQL_CONNECTION_STRING}\n')     # test

print('-------------------------------------------------------------------------------------')
# Register selected variables from OS and JSON providers
config_3 = Config([OSConfigProvider(), JSONConfigProvider()])
print(config_3.register("TEMP"))
print(config_3.register("SQL_CONNECTION_STRING", path='../../envs_config/dev.json'))
print()
print(f'TEMP -> {config_3.TEMP}')     # test
print(f'SQL_CONNECTION_STRING -> {config_3.SQL_CONNECTION_STRING}')     # test
print('-------------------------------------------------------------------------------------')
