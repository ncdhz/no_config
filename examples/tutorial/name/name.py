from no_config import Config
from os import path

@Config(name='app.user')
class User:
    password = None
    username = None

if __name__ == '__main__':
    Config.init(path.join(path.dirname(__file__), 'name.yaml'))
    print(User.password)
    print(User.username)
