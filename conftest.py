import pytest
from src.config.config import Config, JSONConfigProvider, OSConfigProvider
from src.models.data_time import DataTime
from src.models.user import User
from src.applications.git_hub_api import GitHubApi


# Register system environment variables (all)
system_configuration = Config([OSConfigProvider()])
system_configuration.register(item_key='all')

# Register JSON data configuration
json_configuration = Config([JSONConfigProvider()])
json_configuration.register(item_key="BASE_URL", json_path='../envs_config/dev.json')
json_configuration.register(item_key="SQL_CONNECTION_STRING", json_path='../envs_config/dev.json')


# Print date and time execution
@pytest.fixture(scope='session')
def time():
    yield
    time = DataTime()
    print(f'\n\nDate: {time.data()} \t Time: {time.hour()}')


# Generate, use and delete user
@pytest.fixture(scope='function')
def user(name, surname):
    new_user = User(name, surname)
    yield new_user
    del new_user


# Login and logout user
@pytest.fixture()
def api(username):
    api = GitHubApi()
    api.login(username)
    yield api
    api.logout(username)
