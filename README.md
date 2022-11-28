# TEST FRAMEWORK


## Source
[![alt text](https://miro.medium.com/max/719/0*LqBi2dONH28oTKVX.png)](https://github.com/sergii-butenko-gl/talend-eng-II)


## Technologies
- Python
- Pytest
- Requests
- Selenium


## Structure
- /envs_config -> applications data
- /src
  - /applications -> applications
  - /config -> framework config
  - /models -> applications classes
  - /pages -> specific pages models
  - /providers -> data providers
    - /browsers -> browsers providers
    - /data -> data providers
- /tests -> applications and framework tests

| File                    | Description                             |
|-------------------------|-----------------------------------------|
| api_data.py             | Data used by GitHub API application     |
| json_provider_data.json | Data used by JSON provider              |
| base_ui.py              | Basic user interface operations class   |
| github_api.py           | GitHub API operations class             |
| github_ui.py            | GitHub UI operations class              |
| config.py               | Framework data configurator             | 
| data_time.py            | Current data and time generator model   |
| user.py                 | User model                              |
| login_page.py           | GitHub login page object model          |
| reset_password_page.py  | GitHub reset password page object model |
| base_browser.py         | Parent class for browser providers      |
| browser_provider.py     | Browsers UI driver provider             |
| chrome_provider.py      | Chrome UI driver provider               |
| edge_provider.py        | Edge UI driver provider                 |
| firefox_provider.py     | Firefox UI driver provider              |
| base_provider.py        | Parent class for data providers         |
| json_provider.py        | JSON data provider                      |
| os_provider.py          | System environment variables provider   |
| test_config.py          | Framework config data tests             |
| test_github_api.py      | GitHub API tests                        |
| test_github_ui.py       | GitHub UI tests                         |
| test_input_type.py      | Input data types tests                  |
| conftest.py             | Fixtures used by tests                  |
| pytest.ini              | Pytest settings                         |



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
# All config tests
$ pytest ./tests/test_config.py

# System config tests
$ pytest ./tests/test_config.py -k TestsSystem

# Windows path tests
$ pytest ./tests/test_config.py -m windows

# JSON config tests
$ pytest ./tests/test_config.py -k TestsJSON

# User tests
$ pytest ./tests/test_config.py -k TestsUser

# GitHub API tests
$ pytest ./tests/test_github_api.py -k TestsGitHubAPI

# GitHub UI tests
$ pytest ./tests/test_github_ui.py -k TestsGitHubUI
$ pytest ./tests/test_github_ui.py -k TestsGitHubUI --browser chrome/edge/firefox
```

## Author
Przemysław Szpak\
przemyslaw.szpak@globallogic.com