## 开始使用

> 通过带括号的修饰器能更好的加强编辑器的提示功能，此例子在[examples/tutorial/start/start.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/start/start.py)中。

1. 配置文件[examples/tutorial/start/start.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/start/start.yaml)

    ```yaml
    user:
        username: ncdhz-start
        password: ncdhz-start
    ```

2. 源码文件[examples/tutorial/start/start.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/start/start.py)

    ```python
    from no_config import Config
    from os import path

    @Config()
    class User:
        password = None
        username = None

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'start.yaml'))
        print(User.password)
        print(User.username)
    ```

## 文件类型

> `no_config`支持`yaml`、`json`和`toml`三种文件类型，通过`Config.init(file_type='yaml/json/toml')`指定。

1. `json`配置文件[examples/tutorial/file_type/file_type.json](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/file_type/file_type.json)

    ```json
    {
        "user": {
            "username": "ncdhz-json",
            "password": "ncdhz-json"
        }
    }
    ```

2. `toml`配置文件[examples/tutorial/file_type/file_type.toml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/file_type/file_type.toml)

    ```toml
    [user]
    username='ncdhz-toml'
    password='ncdhz-toml'
    ```

3. 源码文件[examples/tutorial/file_type/file_type.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/file_type/file_type.py)

    ```python
    from no_config import Config
    from os import path

    @Config()
    class User:
        password = None
        username = None

    if __name__ == '__main__':
        current_dir = path.dirname(__file__)
        Config.init(path.join(current_dir, 'file_type.json'), file_type='json')
        print(User.password)
        print(User.username)
        Config.init(path.join(current_dir, 'file_type.toml'), file_type='toml')
        print(User.password)
        print(User.username)
    ```

## 多个目标

> 多个类作为配置目标，也只需要一行代码就能解决。

1. 配置文件[examples/tutorial/multitarget/multitarget.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/multitarget/multitarget.yaml)

    ```yaml
    user:
        password: ncdhz-multiple-target
        username: ncdhz-multiple-target

    app:
        name: multiple-target-name
        id: multiple-target-id
    ```

2. 源码文件[examples/tutorial/multitarget/multitarget.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/multitarget/multitarget.py)

    ```python
    from no_config import Config
    from os import path

    @Config()
    class User:
        password = None
        username = None

    @Config()
    class App:
        name = None
        id = None

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'multitarget.yaml'))
        print(User.password)
        print(User.username)
        print(App.name)
        print(App.id)
    ```


## 实体映射

> 当某个字段是一个实体时，可以通过让字段等于实体的方式映射配置。通过此方式映射的属性都是静态的。

1. 配置文件[examples/tutorial/class_mapper/class_mapper.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/class_mapper/class_mapper.yaml)

    ```yaml
    app:
        name: class-mapper-name
        user:
            username: ncdhz-class-mapper
    ```

2. 源码文件[examples/tutorial/class_mapper/class_mapper.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/class_mapper/class_mapper.py)

    ```python
    from no_config import Config
    from os import path

    class User:
        username = None

    @Config()
    class App:
        name = None
        user = User

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'class_mapper.yaml'))
        print(App.name)
        print(App.user.username)
        print(User.username)
    ```

## 方法映射

> 需要对配置信息进行处理时可以直接指定一个方法。

1. 配置文件[examples/tutorial/function_mapper/function_mapper.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/function_mapper/function_mapper.yaml)

    ```yaml
    app:
        name: function-mapper-name
    ```

2. 源码文件[examples/tutorial/function_mapper/function_mapper.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/function_mapper/function_mapper.py)

    ```python
    from no_config import Config
    from os import path

    def analysis(name):
        return name.split('-')

    @Config()
    class App:
        name = analysis

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'function_mapper.yaml'))
        print(App.name)
    ```
    