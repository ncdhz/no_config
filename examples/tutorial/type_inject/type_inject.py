from no_config import Config
from os import path

class User:
    username = None

@Config(type=dict(user=User))
class App:
    name = None
    user = None

if __name__ == '__main__':
    Config.init(path.join(path.dirname(__file__), 'type_inject.yaml'))
    print(App.name)
    print(App.user.username)
    print(User.username)