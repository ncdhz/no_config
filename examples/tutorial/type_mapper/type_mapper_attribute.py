from no_config import Config
from os import path

class User:
    pass

@Config(type=dict(user=User))
class App:
    name = None
    user = None

if __name__ == '__main__':
    Config.init(path.join(path.dirname(__file__), 'type_mapper.yaml'))
    print(App.name)
    # 这里username任然会映射成功
    print(App.user.username)
