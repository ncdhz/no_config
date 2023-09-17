from no_config import Config
from os import path

def analysis(name):
    return name.split('-')

@Config()
class App:
    name = analysis

if __name__ == '__main__':
    Config.init(path.join(path.dirname(__file__), 'function_mapper.yaml'))
    print(App.name)