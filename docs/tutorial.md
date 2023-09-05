## 基础使用

> 通过带括号的修饰器能更好的加强编辑器的提示功能，此例子在[examples/tutorial/base/base.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/base/base.py)中。

1. 配置文件[examples/tutorial/base/base.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/base/base.yaml)

    ```yaml
    user:
        username: base
        password: base
    ```

2. 源码文件[examples/tutorial/base/base.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/base/base.py)

    ```python
    from no_config import Config
    from os import path

    @Config()
    class User:
        password = None
        username = None

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'base.yaml'))
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

    ```py
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

1. 配置文件[examples/tutorial/multiple_target/multiple_target.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/multiple_target/multiple_target.yaml)

    ```yaml
    user:
        password: ncdhz-multiple-target
        username: ncdhz-multiple-target

    app:
        name: multiple-target-name
        id: multiple-target-id
    ```

2. 源码文件[examples/tutorial/multiple_target/multiple_target.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/multiple_target/multiple_target.py)

    ```py
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
        Config.init(path.join(path.dirname(__file__), 'multiple_target.yaml'))
        print(User.password)
        print(User.username)
        print(App.name)
        print(App.id)
    ```

## 配置名字

> 在`no_config`中，如果不指定名字，默认使用类名的下划线格式，如类名`UserName`对应`user_name`，`User`对应的就是`user`。如下例子可以通过`name`属性设置配置名字，其中`.`表示下一级，`app.user`表示`app`第一级`user`第二级对应的配置，如配置文件所示。

1. 配置文件

    ```yaml
    app:
        user:
            password: ncdhz-name
            username: ncdhz-name
    ```

2. 源码文件

    ```py
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