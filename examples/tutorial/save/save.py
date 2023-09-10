from no_config import Config
from os import path

class Password:
    def __init__(self):
        self.password = 'password'

@Config(type=dict(password=Password))
class User:
    password = Password()
    username = None

if __name__ == '__main__':
    Config.init(path.join(path.dirname(__file__), 'save.yaml'))
    Config.save()
    Config.save(file_path='config.yaml')
    Config.save(file_path='config.json', file_type='json')
    Config.save(file_path='config.toml', file_type='toml')
