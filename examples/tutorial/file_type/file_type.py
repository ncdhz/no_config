from no_config import Config
from os import path

@Config()
class User:
    password = None
    username = None

if __name__ == '__main__':
    
    current_dir = path.dirname(__file__)
    Config.init(path.join(current_dir, 'file_type.json'), file_type='json')
    print(User.password)
    print(User.username)
    Config.init(path.join(current_dir, 'file_type.toml'), file_type='toml')
    print(User.password)
    print(User.username)
