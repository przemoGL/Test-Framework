import requests
from src.data.api_data import GITHUB_API_URL, GITHUB_RECOMMENDED_ACCEPT_HEADER

logged_users = []


class GitHubApi:
    def login(self, user_name):
        logged_users.append(user_name)
        print(f"\nUser '{user_name}' logged in")

    def logout(self, user_name):
        logged_users.remove(user_name)
        print(f"\nUser '{user_name}' logged out")

    def get_repository_info(self, repository_path):
        r = requests.get(
            url=GITHUB_API_URL + "search/repositories",
            headers=GITHUB_RECOMMENDED_ACCEPT_HEADER,
            params={'q': repository_path}
        )
        r.raise_for_status()
        return r.json()

    def get_user_repositories(self, owner, sort_by):
        r = requests.get(
            url=GITHUB_API_URL + "users/" + owner + "/repos",
            headers=GITHUB_RECOMMENDED_ACCEPT_HEADER,
            params={'sort': sort_by}
        )
        r.raise_for_status()
        return r.json()


# x = GitHubApi().get_repository_info("przemoGL/training")
# pprint.pprint(x)
# y = GitHubApi().get_user_repositories(owner="przemoGL", sort_by="created")
# pprint.pprint(y)
