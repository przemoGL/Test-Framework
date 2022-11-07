# BUILDING FRAMEWORK


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
    - base_provider.py
    - os_provider.py
    - json_provider.py
  - /data
  - /models
  - /providers
- /tests
  - test_input_type.py

| File               | Description                                     |
|--------------------|-------------------------------------------------|
| config.py          | Configurator of registering data from providers | 
| os_provider.py     | System environment variables provider           |
| json_provider.py   | JSON data provider                              |
| base_provider.py   | Verifier of correctness provider configuration  |
| dev.json           | Data used by JSON provider                      |
| test_input_type.py | Tests verifying correctness of data type input  |


## Environment preparing
```bash
$ pip install -r requirements.txt
```

## Providers instances creating
```
> config_name = Config([provider_objects])
```

## Registering data from provider
```
> config_name.register('data_key', path='optional_file_path')
```

## Reading registered data
```
> config_name.data_key
```


## Tests running
```bash
$ pytest ./tests/test_input_type.py
```

## Author
Przemysław Szpak\
przemyslaw.szpak@globallogic.com