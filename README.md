# TESTING FRAMEWORK


## Source
[![alt text](https://miro.medium.com/max/719/0*LqBi2dONH28oTKVX.png)](https://github.com/sergii-butenko-gl/talend-eng-II)


## Technologies
| Tool   | Version |
|--------|---------|
| Python | 3.11    | 
| Pytest | 7.2.0   |


## Structure
- /envs_config
    - dev.json
- /src
  - /config
    - config.py
  - /data
  - /models
    - time_class.py
  - /providers
    - base_provider.py
    - os_provider.py
    - json_provider.py
- /tests
  - test_configuration.py
  - test_input_type.py
- conftest.py
- pytest.ini

| File                  | Description                                     |
|-----------------------|-------------------------------------------------|
| config.py             | Configurator of registering data from providers | 
| os_provider.py        | System environment variables provider           |
| json_provider.py      | JSON data provider                              |
| base_provider.py      | Verifier of correctness provider configuration  |
| dev.json              | Data used by JSON provider                      |
| time_class.py         | Current time generator model                    |
| test_configuration.py | Tests verifying data configuration              |
| test_input_type.py    | Tests verifying correctness of data type input  |
| conftest.py           | Fixtures to tests                               |
| pytest.ini            | Tests warning ignoring settings                 |



## Environment preparing
```bash
$ pip install -r requirements.txt
```

## Data providers configurating
```python
# provider initializing
> config_name = Config([OSConfigProvider()])
> config_name = Config([JSONConfigProvider()])
> config_name = Config([OSConfigProvider(), JSONConfigProvider()])

# data registering
> config_name.register(item_key='all')
> config_name.register(item_key='<data_key>')
> config_name.register(item_key='all', json_path='<json_file_path>')

# data getting
> config_name.data_key
```


## Tests running
```bash
# All configuration tests
$ pytest ./tests/test_configuration.py

# System configuration tests
$ pytest ./tests/test_configuration.py -m system

# Windows directory tests
$ pytest ./tests/test_configuration.py -m windows_dir

# JSON configuration tests
$ pytest ./tests/test_configuration.py -m json
```

## Author
Przemysław Szpak\
przemyslaw.szpak@globallogic.com