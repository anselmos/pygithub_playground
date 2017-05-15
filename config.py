"""
Config Reader
"""
import ConfigParser

CONFIG_FILE_PATH = ".pygithub.conf"
class Config(object):

    def __init__(self):
        self.config_parser = ConfigParser.RawConfigParser()
        self.config_parser.read(CONFIG_FILE_PATH)

    def get_name(self):
        "returns username from config"
        return self.config_parser.get('main', 'username')

    def get_pass(self):
        "returns password from config"
        return self.config_parser.get('main', 'password')

    def get_repo(self):
        "returns repository from config"
        return self.config_parser.get('main', 'repository')
