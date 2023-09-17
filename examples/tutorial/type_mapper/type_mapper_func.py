from no_config import Config
from os import path

def split_name(name):
    return name.split('-')

@Config(type=dict(name=split_name))
class App:
    name = None

if __name__ == '__main__':
    Config.init(path.join(path.dirname(__file__), 'type_mapper_func.yaml'))
    print(App.name)