# BUILDING FRAMEWORK


## Source
[![alt text](https://ipatryk.pl/wp-content/uploads/2017/06/github.png)](https://github.com/sergii-butenko-gl/talend-eng-II)


## Technologies
- Python 3.11
- Pytest 7.2.0


## Structure
- /envs_config
    - dev.json
- /src
  - /config
    - config.py
  - /data
  - /models
  - /providers
- /tests
  - test_input_type.py

### /src/config/config.py
Configuration of framework.
Allows to register specific data from system environment variables and JSON files.

### /envs_config
Storage of files with providers data.

### /tests/test_input_type.py
Tests to verify correctness of input data with Python data types.


## Tests running
```bash
$ pytest ./tests/test_input_type.py
```