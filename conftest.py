from src.config.config import Config, OSConfigProvider, JSONConfigProvider
from src.models.time_class import Time
import pytest


# Register system environment variables (all)
@pytest.fixture
def system_configuration():
    system_configuration = Config([OSConfigProvider()])
    system_configuration.register(item_key='all')
    yield system_configuration
    print('\nSystem data.')


# Register JSON data configuration
@pytest.fixture
def json_configuration():
    json_configuration = Config([JSONConfigProvider()])
    json_configuration.register(item_key="BASE_URL", json_path='../envs_config/dev.json')
    json_configuration.register(item_key="SQL_CONNECTION_STRING", json_path='../envs_config/dev.json')
    yield json_configuration
    print('\nJSON data.')


# Print date and time execution
@pytest.fixture(scope='session')
def time():
    time = Time()
    yield
    print(f'Date: {time.data()} \t Time: {time.hour()}')
