import pytest
from src.config.config import config


@pytest.mark.usefixtures("time")
class TestsSystem:
    @pytest.mark.windows
    def test_windows_directory(self):
        assert config.WINDIR == "C:\\Windows"

    @pytest.mark.windows
    def test_path_ext(self):
        assert ".CMD" in config.PATHEXT

    def test_onedrive(self):
        assert hasattr(config, "ONEDRIVE")

    @pytest.mark.xfail(reason="Compared user name is correct")
    def test_user_negative(self):
        assert config.USERNAME != "przemyslaw.szpak"

    @pytest.mark.skip("Using from terminal causes failing")
    def test_python(self):
        assert int(config.PYTHONUNBUFFERED) == 1


class TestsJSON:
    def test_sql_connection(self):
        assert config.SQL_CONNECTION_STRING.startswith("SQL://")

    def test_base_url(self):
        assert "google" in config.BASE_URL


class TestsUser:
    @pytest.mark.parametrize("name, surname, expected_email",
                             [["Przemyslaw", "Szpak", 'przemyslaw.szpak@globallogic.com'],
                              ["Jan", "Kowalski", 'jan.kowalski@globallogic.com']])
    def test_email(self, user, expected_email):
        assert user.email == expected_email

    @pytest.mark.parametrize("name, surname",
                             [["Przemyslaw", "Szpak"],
                              ["Jan", "Kowalski"]])
    def test_length(self, user):
        assert len(str(user)) == len(user.name) + len(user.surname) + len(user.email) + 1
