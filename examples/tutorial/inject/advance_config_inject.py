from no_config import Inject

@Inject
class User:
    def __init__(self, username, password):
        pass

@Inject(type=dict(user=User))
class App:
    def __init__(self, id, user):
        pass

if __name__ == '__main__':

    config_inject = App(config_inject=dict(
        id='config-inject-app-id',
        user=dict(
            username='config-inject-username',
            password='config-inject-password'
        )
    ))
    print(config_inject.id)
    print(config_inject.user.username)
    print(config_inject.user.password)