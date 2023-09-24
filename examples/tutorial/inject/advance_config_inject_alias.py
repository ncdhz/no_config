from no_config import Inject

@Inject
class User:
    def __init__(self, username, password):
        pass

@Inject(type=dict(user=User), config_inject='config_inject_alias')
class App:
    def __init__(self, id, user):
        pass

if __name__ == '__main__':

    config_inject_alias = App(config_inject_alias=dict(
        id='config_inject_alias_app_id',
        user=dict(
            username='config_inject_alias_username',
            password='config_inject_alias_password'
        )
    ))
    print(config_inject_alias.id)
    print(config_inject_alias.user.username)
    print(config_inject_alias.user.password)