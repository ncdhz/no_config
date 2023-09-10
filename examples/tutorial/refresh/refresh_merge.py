from no_config import Config
from os import path

@Config()
class User:
    password = None
    username = None

if __name__ == '__main__':
    Config.init(path.join(path.dirname(__file__), 'refresh.yaml'))
    print(Config.get_config())
    Config.refresh({
        'user': {
            'password': 'password'
        }
    }, merge=True)
    print(Config.get_config())
