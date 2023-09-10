from no_config import Config
from os import path

@Config()
class User:
    password = 'password'
    username = None

if __name__ == '__main__':
    Config.init(path.join(path.dirname(__file__), 'config.yaml'))
    print(Config.get_config())
    print(Config.get_all_config())