from github import Github
from config import Config

class Looping(object):
    """
    Main looping object. Methods available:
    - over_issues- Loops over all issues available for user
    - over_repository_issues - Loops only over issues of repository set in config
    """


    def __init__(self):
        self.conf = Config()
        self.g = Github(self.conf.get_name(), self.conf.get_pass())

    def over_repository_issues(self):
        for repo in self.g.get_user().get_repos():
            if repo.name == self.conf.get_repo():
                for issue in repo.get_issues():
                    print issue

    def over_issues(self):
        for repo in self.g.get_user().get_repos():
            print repo.name
            for issue in repo.get_issues():
                print issue

def main():
    loop_object = Looping()
    loop_object.over_issues()
    loop_object.over_repository_issues()

if __name__ == "__main__":
    main()
