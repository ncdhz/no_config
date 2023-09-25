from no_config import Config
from os import path

class User:
    def __init__(self, username):
        username += '-xxx'
        self.username = username

@Config(type=dict(user=User))
class App:
    name = None
    user = None

if __name__ == '__main__':
    Config.init(path.join(path.dirname(__file__), 'type_mapper.yaml'))
    print(App.name)
    print(App.user.username)