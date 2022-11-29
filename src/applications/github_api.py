import requests
from src.config.config import config


class GitHubApi:
    GITHUB_RECOMMENDED_ACCEPT_HEADER = {"accept": "application/vnd.github+json"}

    @staticmethod
    def login(user_name):
        """
        User logging-in procedure.
        :param user_name: User name to log-in [str]
        """
        # Any log-in logic
        print(f"\nUser '{user_name}' logged in")

    @staticmethod
    def logout(user_name):
        """
        User logging-out procedure.
        :param user_name: User name to log-out [str]
        """
        # Any log-out logic
        print(f"\nUser '{user_name}' logged out")

    def get_repository_info(self, repository_path):
        """
        Find repository details - amount of found repositories and information like ID, creation date, etc.
        Documentation: https://docs.github.com/en/rest/search#search-repositories
        :param repository_path: path to repository (format: owner/name) or name only (multiple results possible) [str]
        :return: repository info [dict]
        """
        r = requests.get(
            url=config.GITHUB_API_URL + "search/repositories",
            headers=self.GITHUB_RECOMMENDED_ACCEPT_HEADER,
            params={'q': repository_path}
            )
        r.raise_for_status()
        if r.json()['total_count'] == 0:
            raise ValueError("No repository found")
        else:
            return r.json()

    def get_user_repositories(self, owner, sort_by="full_name"):
        """
        Get all public repositories of given owner.
        Documentation: https://docs.github.com/en/rest/repos/repos#list-repositories-for-a-user
        :param owner: desirable owner of repositories [str]
        :param sort_by: type of sorting result - can be full_name (default), created, updated or pushed [str]
        :return: found repositories with their details [list]
        """
        r = requests.get(
            url=config.GITHUB_API_URL + "users/" + owner + "/repos",
            headers=self.GITHUB_RECOMMENDED_ACCEPT_HEADER,
            params={'sort': sort_by}
            )
        r.raise_for_status()
        return r.json()
