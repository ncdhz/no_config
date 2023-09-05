from no_config import Config


@Config()
class User:
    password = None
    username = None


class App:
    name = None
    id = None


if __name__ == '__main__':
    Config.init('examples/test_tutorial_multiple_target.yaml')
    print(User.password)
    print(User.username)
