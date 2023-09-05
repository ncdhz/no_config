from no_config import Config
from os import path

# 使用类修饰能更好的利用编辑器的提示功能
@Config()
class User:
    password = None
    username = None

if __name__ == '__main__':
    Config.init(path.join(path.dirname(__file__), 'class.yaml'))
    print(User.password)
    print(User.username)
