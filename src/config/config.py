import logging
from src.providers.data.os_provider import OSConfigProvider
from src.providers.data.json_provider import JSONConfigProvider

logging.basicConfig(
    filename='test.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s')
log = logging.getLogger()


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

    def register(self, item_key='all', json_path=None):
        """
        Method to registering wanted data to configs [dict] from providers.
        :param item_key: name (key) of wanted variable [str], default 'None' means all variables
        :param json_path: path of file to registering data from [str], default 'None' means provider do not require file
        :return: registered data [str]
        """
        for provider in self.config_providers:
            # register all data
            if item_key == 'all':
                self.configs = self.configs | provider.get(item_key, json_path)
                print(f'Registered all data from {str(provider)}.')
            # register selected data from chosen provider
            elif (json_path is None and isinstance(provider, OSConfigProvider)) or \
                    (json_path is not None and isinstance(provider, JSONConfigProvider)):
                item_value = provider.get(item_key, json_path)
                if item_value is not None:
                    self.configs[item_key] = item_value
                    log.info(f'Registered {item_key} from {str(provider)}.')
                    print(f'Registered {item_key} from {str(provider)}.')
                else:
                    log.warning(f"Can not register {item_key} - key not exist in providers.")
                    print(f"Can not register {item_key} - key not exist in providers.")

        self.set_attributes()
        return f'Registered attributes: {self.configs}'

    def set_attributes(self):
        """
        Method to set registered data records as instance attributes.
        """
        for item_key, item_value in self.configs.items():
            setattr(self, item_key, item_value)

        log.info(f'Registered attributes: {self.configs}')

    def __str__(self):
        return f'{self.configs}'


config = Config([OSConfigProvider(), JSONConfigProvider()])
config.register(item_key='WINDIR')
config.register(item_key='PATHEXT')
config.register(item_key='ONEDRIVE')
config.register(item_key='USERNAME')
config.register(item_key='PYTHONUNBUFFERED')
config.register(item_key='BASE_URL',
                json_path='../envs_config/dev.json')  # path from tests perspective
config.register(item_key='SQL_CONNECTION_STRING',
                json_path='../envs_config/dev.json')  # path from tests perspective
config.register(item_key='GITHUB_MAIN_URL',
                json_path='../envs_config/dev.json')  # path from tests perspective
config.register(item_key='GITHUB_API_URL',
                json_path='../envs_config/dev.json')  # path from tests perspective
