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
    current_dir = path.dirname(__file__)
    Config.init([path.join(current_dir, 'multifile_one.yaml'), 
                 dict(path=path.join(current_dir, 'multifile_two.json'), type='json')])
    print(User.password)
    print(User.username)
    print(App.name)
    print(App.id)