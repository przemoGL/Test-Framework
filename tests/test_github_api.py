import pytest


class TestsGitHubAPI:

    @pytest.mark.parametrize("username, repository_path",
                             [["pszpak", "przemoGL/Test-Framework"]])
    def test_repository_name(self, github_api, repository_path):
        body = github_api.get_repository_info(repository_path)
        assert body['items'][0]['name'] == "Test-Framework"

    @pytest.mark.parametrize("username, username_path_param, sort",
                             [["pszpak", "przemoGL", "created"]])
    def test_repositories_order(self, github_api, username_path_param, sort):
        body = github_api.get_user_repositories(username_path_param, sort)
        assert body[0]['id'] < body[1]['id']

    @pytest.mark.parametrize("username, username_path_param, sort, direction",
                             [["pszpak", "przemoGL", "created", "desc"]])
    def test_repositories_sorting_direction(self, github_api, username_path_param, sort, direction):
        body = github_api.get_user_repositories(username_path_param, sort, direction)
        assert body[0]['id'] > body[1]['id']
