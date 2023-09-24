from no_config import Config
from os import path

@Config()
class User:
    password = None
    username = None

@Config()
class App:
    name = None
    id = None

if __name__ == '__main__':
    Config.init(path.join(path.dirname(__file__), 'multitarget.yaml'))
    print(User.password)
    print(User.username)
    print(App.name)
    print(App.id)
