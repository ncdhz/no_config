## 简介

`no_config`库保存配置时采用的是`属性探测`，通过递归拿到获取属性。如下面例子，如果没有添加`self.username=username`和`self.password=password`代码，在保存配置时将不会保存`username`和`password`的配置。显然在初始化构建配置类时，会增加很多无用的代码，这是一种吃力不讨好的工作。

```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
@Config()
class App:
    user = User('ncdhz', 'ncdhz')
```

## @Inject使用

> `@Inject`添加在方法上可以轻松的完成参数到属性的注入。

1. 源码文件[examples/tutorial/inject/start.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/inject/start.py)

    ```python
    from no_config import Inject, Config

    @Inject
    class User:
        def __init__(self, username, password):
            # 这里可以添加其它代码对username和password处理
            pass

    @Config
    class App:
        user = User('ncdhz', 'ncdhz')

    if __name__ == '__main__':
        print(Config.get_all_config())
        print(App.user.username)
        print(App.user.password)
    ```

## 类注入

> 实际开发中，类的初始化参数可能是某个类，可以通过`@Inject(user=User)`的方式进行指定。

1. 源码文件[examples/tutorial/inject/advance_class.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/inject/advance_class.py)

    ```python
    from no_config import Inject

    @Inject
    class User:
        def __init__(self, username, password):
            pass

    @Inject(user=User)
    class App:
        def __init__(self, id, user):
            pass

    if __name__ == '__main__':
        app = App('app_id', dict(username='username', password='password'))
        print(app.id)
        print(app.user.username)
        print(app.user.password)
    ```

## 方法注入

> 如果需要对参数进行一些处理，可以使用如下方式。

1. 源码文件[examples/tutorial/inject/advance_func.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/inject/advance_func.py)

    ```python
    from no_config import Inject

    def split_name(name):
        return name.split('-')

    @Inject(name=split_name)
    class App:
        def __init__(self, id, name):
            pass

    if __name__ == '__main__':
        app = App('app_id', 'ncdhz-inject-func')
        print(app.id)
        print(app.name)
    ```