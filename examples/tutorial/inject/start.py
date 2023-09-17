from no_config import Inject, Config

@Inject
class User:
    def __init__(self, username, password):
        pass

@Config
class App:
    user = User('ncdhz', 'ncdhz')

if __name__ == '__main__':
    print(Config.get_all_config())
    print(App.user.username)
    print(App.user.password)