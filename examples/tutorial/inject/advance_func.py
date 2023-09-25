from no_config import Inject

def split_name(name):
    return name.split('-')

@Inject(type=dict(name=split_name))
class App:
    def __init__(self, id, name):
        pass

if __name__ == '__main__':
    app = App('app-id', 'ncdhz-inject-func')
    print(app.id)
    print(app.name)