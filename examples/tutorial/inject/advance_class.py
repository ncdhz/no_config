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
    app = App('app-id', dict(username='username', password='password'))
    print(app.id)
    print(app.user.username)
    print(app.user.password)
