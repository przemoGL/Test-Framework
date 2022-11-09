from src.providers.os_provider import OSConfigProvider
from src.providers.json_provider import JSONConfigProvider


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

    def register(self, item_key=None, json_path=None):
        """
        Method to registering wanted data to configs [dict] from providers.
        :param item_key: name (key) of wanted variable [str], default 'None' means all variables
        :param json_path: path of file to registering data from [str], default 'None' means provider do not require file
        :return: registered data [str]
        """
        for provider in self.config_providers:
            # get all data from provider
            if item_key == 'all':
                self.configs = self.configs | provider.get(item_key, json_path)
                print(f'Registered all data from {str(provider)}.')
            # get specific data from OS or JSON provider
            elif (json_path is None and isinstance(provider, OSConfigProvider)) or \
                 (json_path is not None and isinstance(provider, JSONConfigProvider)):
                item_value = provider.get(item_key, json_path)
                if item_value is not None:
                    self.configs[item_key] = item_value
        self.set_attributes()
        return f'Registered: {self.configs}'

    def set_attributes(self):
        """
        Method to set registered data records as instance attributes.
        """
        for item_key, item_value in self.configs.items():
            setattr(self, item_key, item_value)

    def __str__(self):
        return f'{self.configs}'


if __name__ == "__main__":
    print('-------------------------------------------------------------------------------------')
    # Register all variables from OS provider
    config_1 = Config([OSConfigProvider()])
    print(config_1.register(item_key='all'))
    print()
    print(f'TEMP -> {config_1.TEMP}')                                                  # test

    print('-------------------------------------------------------------------------------------')
    # Register all variables from OS and JSON providers
    config_2 = Config([OSConfigProvider(), JSONConfigProvider()])
    print(config_2.register(item_key='all', json_path='../../envs_config/dev.json'))
    print()
    print(f'TEMP -> {config_1.TEMP}')                                                  # test
    print(f'SQL_CONNECTION_STRING -> {config_2.SQL_CONNECTION_STRING}')                # test

    print('-------------------------------------------------------------------------------------')
    # Register selected variables from OS and JSON providers
    config_3 = Config([OSConfigProvider(), JSONConfigProvider()])
    print(config_3.register(item_key="TEMP"))
    print(config_3.register("SQL_CONNECTION_STRING", json_path='../../envs_config/dev.json'))
    print()
    print(f'TEMP -> {config_3.TEMP}')                                                  # test
    print(f'SQL_CONNECTION_STRING -> {config_3.SQL_CONNECTION_STRING}')                # test
    print('-------------------------------------------------------------------------------------')
