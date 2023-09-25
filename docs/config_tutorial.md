## 配置名字

> 在`no_config`中，如果不指定名字，默认使用类名的下划线格式，如类名`UserName`对应`user_name`，`User`对应的就是`user`。如下例子可以通过`name`属性设置配置名字，其中`.`表示下一级，`app.user`表示`app`第一级`user`第二级对应的配置，如配置文件所示。

1. 配置文件[examples/tutorial/name/name.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/name/name.yaml)

    ```yaml
    app:
        user:
            password: ncdhz-name
            username: ncdhz-name
    ```

2. 源码文件[examples/tutorial/name/name.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/name/name.py)

    ```python
    from no_config import Config
    from os import path

    @Config(name='app.user')
    class User:
        password = None
        username = None

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'name.yaml'))
        print(User.password)
        print(User.username)
    ```


## 类别映射

> 通过`Config`中的`type`参数可以配置类中某静态属性属于哪个实体类，其中实体的映射使用的初始化函数。

1. 配置文件[examples/tutorial/type_mapper/type_mapper.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/type_mapper/type_mapper.yaml)

    ```yaml
    app:
        name: type-mapper-name
        user:
            username: ncdhz-type-mapper
    ```

2. 源码文件[examples/tutorial/type_mapper/type_mapper.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/type_mapper/type_mapper.py)

    ```python
    from no_config import Config
    from os import path

    class User:
        username = None

    @Config(type=dict(user=User))
    class App:
        name = None
        user = None

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'type_mapper.yaml'))
        print(App.name)
        print(App.user.username)
        # 这里打印为空，说明type指定的映射方式调用的是初始化函数
        print(User.username)
    ```

## 映射加工

> 类别映射中可以通过初始化函数对映射的配置进行加工。

1. 源码文件[examples/tutorial/type_mapper/type_mapper_handle.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/type_mapper/type_mapper_handle.py)

    ```python
    from no_config import Config
    from os import path

    class User:
        def __init__(self, username):
            username += '-xxx'
            self.username = username

    @Config(type=dict(user=User))
    class App:
        name = None
        user = None

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'type_mapper.yaml'))
        print(App.name)
        print(App.user.username)
    ```

## 属性映射

1. 源码文件[examples/tutorial/type_mapper/type_mapper_attribute.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/type_mapper/type_mapper_attribute.py)
    
    > 属性映射指配置文件中所有值都会映射到`self`下面。

    ```python
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
        # 这里username仍然会映射成功
        print(App.user.username)
    ```


## 方法映射

> 如果你想对某个属性进行处理，那么你可以在`type`中给它指定一个处理函数。

1. 配置文件[examples/tutorial/type_mapper/type_mapper_func.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/type_mapper/type_mapper_func.yaml)

    ```yaml
    app:
        name: type-mapper-name
    ```

2. 源码文件[examples/tutorial/type_mapper/type_mapper_func.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/type_mapper/type_mapper_func.py)

    ```python
    from no_config import Config
    from os import path

    def split_name(name):
        return name.split('-')

    @Config(type=dict(name=split_name))
    class App:
        name = None

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'type_mapper_func.yaml'))
        print(App.name)
    ```
