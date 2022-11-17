import pytest


class TestsAPI:

    @pytest.mark.parametrize("username, repository_path",
                             [["pszpak", "przemoGL/training"]])
    def test_repository_name(self, api, repository_path):
        body = api.get_repository_info(repository_path)
        assert body['items'][0]['name'] == "training"

    @pytest.mark.parametrize("username, owner, sort_by",
                             [["pszpak", "przemoGL", "created"]])
    def test_repositories_order(self, api, owner, sort_by):
        body = api.get_user_repositories(owner, sort_by)
        assert body[0]['id'] > body[1]['id']
