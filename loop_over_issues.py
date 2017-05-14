from github import Github
import ConfigParser

config_file_path = ".pygithub.conf"
config_parser = ConfigParser.RawConfigParser()
config_parser.read(config_file_path)
pyname = config_parser.get('main', 'username')
pypass = config_parser.get('main', 'password')

# First create a Github instance:
g = Github(pyname, pypass)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print repo.name
    for issue in repo.get_issues():
        print issue
