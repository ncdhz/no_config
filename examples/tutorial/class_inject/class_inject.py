from no_config import Config
from os import path

class User:
    username = None

@Config()
class App:
    name = None
    user = User

if __name__ == '__main__':
    Config.init(path.join(path.dirname(__file__), 'class_inject.yaml'))
    print(App.name)
    print(App.user.username)
    print(User.username)