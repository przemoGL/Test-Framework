# TEST FRAMEWORK


## Source
[![alt text](https://miro.medium.com/max/719/0*LqBi2dONH28oTKVX.png)](https://github.com/sergii-butenko-gl/talend-eng-II)


## Technologies
| Tool     | Version |
|----------|---------|
| Python   | 3.11    | 
| Pytest   | 7.2.0   |
| Requests | 2.28.1  |
| Selenium | 4.6.0   |


## Structure
- /envs_config -> applications data
- /src
  - /applications -> applications
  - /config -> framework configuration
  - /models -> applications classes
  - /providers -> data providers
    - /browsers -> browsers data providers
- /tests -> applications and framework tests

| File                    | Description                           |
|-------------------------|---------------------------------------|
| api_data.py             | Data used by GitHub API application   |
| json_provider_data.json | Data used by JSON provider            |
| base_ui.py              | Basic user interface operations class |
| github_api.py           | GitHub API operations class           |
| github_ui.py            | GitHub UI operations class            |
| config.py               | Framework data configurator           | 
| data_time.py            | Current data and time generator model |
| user.py                 | User model                            |
| base_browser.py         | Parent class for browser providers    |
| browser_provider.py     | Browsers UI driver provider           |
| chrome_provider.py      | Chrome UI driver provider             |
| edge_provider.py        | Edge UI driver provider               |
| firefox_provider.py     | Firefox UI driver provider            |
| base_provider.py        | Parent class for data providers       |
| json_provider.py        | JSON data provider                    |
| os_provider.py          | System environment variables provider |
| test_configuration.py   | Framework configuration data tests    |
| test_github_api.py      | GitHub API tests                      |
| test_github_ui.py       | GitHub UI tests                       |
| test_input_type.py      | Input data types tests                |
| conftest.py             | Fixtures used by tests                |
| pytest.ini              | Pytest settings                       |



## Environment preparing
```bash
$ pip install -r requirements.txt
```

## Data providers configuring
```python
# provider initializing (possibilities)
> config_name = Config([OSConfigProvider()])
> config_name = Config([JSONConfigProvider()])
> config_name = Config([OSConfigProvider(), JSONConfigProvider()])

# data registering (possibilities)
> config_name.register(item_key='all')
> config_name.register(item_key='<data_key>')
> config_name.register(item_key='all', json_path='<json_file_path>')
> config_name.register(item_key='<data_key>', json_path='<json_file_path>')

# registered data getting
> config_name.data_key
```


## Tests running
```bash
# All configuration tests
$ pytest ./tests/test_configuration.py

# System configuration tests
$ pytest ./tests/test_configuration.py -k TestsSystem

# Windows path tests
$ pytest ./tests/test_configuration.py -m windows

# JSON configuration tests
$ pytest ./tests/test_configuration.py -k TestsJSON

# User tests
$ pytest ./tests/test_configuration.py -k TestsUser

# GitHub API tests
$ pytest ./tests/test_github_api.py -k TestsGitHubAPI

# GitHub UI tests
$ pytest ./tests/test_github_api.py -k TestsGitHubUI
```

## Author
Przemysław Szpak\
przemyslaw.szpak@globallogic.com