import pytest


@pytest.mark.usefixtures("time")

@pytest.mark.system
class TestsSystem:
    @pytest.mark.windows_dir
    def test_windows_directory(self, system_configuration):
        assert system_configuration.WINDIR == 'C:\\Windows'

    @pytest.mark.xfail(reason='Set user is correct')
    def test_user_negative(self, system_configuration):
        assert system_configuration.USERNAME != 'przemyslaw.szpak'

    def test_onedrive(self, system_configuration):
        assert hasattr(system_configuration, 'ONEDRIVE')

    @pytest.mark.skip('Using from terminal causes failing')
    def test_python(self, system_configuration):
        assert int(system_configuration.PYTHONUNBUFFERED) == 1

    @pytest.mark.windows_dir
    def test_path_ext(self, system_configuration):
        assert '.CMD' in system_configuration.PATHEXT


@pytest.mark.json
class TestsJSON:
    def test_sql_connection(self, json_configuration):
        assert json_configuration.SQL_CONNECTION_STRING.startswith('SQL://')

    def test_base_url(self, json_configuration):
        assert 'google' in json_configuration.BASE_URL
