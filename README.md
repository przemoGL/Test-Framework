# BUILDING FRAMEWORK


## Source
[![alt text](https://miro.medium.com/max/719/0*LqBi2dONH28oTKVX.png)](https://github.com/sergii-butenko-gl/talend-eng-II)


## Technologies
- Python 3.11
- Pytest 7.2.0


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

### config.py
Configuration of framework.
Allows to register specific data from providers.

### ._provider.py
Specific data providers configurations.

### /envs_config
Storage of providers data files.

### test_input_type.py
Tests to verify correctness of input data with Python data types.


## Tests running
```bash
$ pytest ./tests/test_input_type.py
```