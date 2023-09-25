## 多个文件

> 实际生产中配置可能会跨配置文件（可以分为固定配置和变化配置），下面演示了两种不同配置文件的整合配置。

1. 配置文件一[examples/tutorial/multifile/multifile_one.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/multifile/multifile_one.yaml)

    ```yaml
    user:
        password: ncdhz-multifile-password
    app:
        name: multifile-name
    ```

2. 配置文件二[examples/tutorial/multifile/multifile_two.json](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/multifile/multifile_two.json)

    ```json
    {
        "user": {
            "username": "ncdhz-multifile-username"
        },
        "app": {
            "id": "multifile-id"
        }
    }
    ```

3. 源码文件[examples/tutorial/multifile/multifile.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/multifile/multifile.py)

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
        current_dir = path.dirname(__file__)
        Config.init([path.join(current_dir, 'multifile_one.yaml'), 
                     dict(path=path.join(current_dir, 'multifile_two.json'), type='json')])
        print(User.password)
        print(User.username)
        print(App.name)
        print(App.id)
    ```

## 文件嵌套

> 文件嵌套通过`Config`的`config_path`属性指定，下面例子中被嵌套的文件为配置文件二，指定的路径为`config.path`。

1. 配置文件一[examples/tutorial/multifile/multifile_sub_one.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/multifile/multifile_sub_one.yaml)

    ```yaml
    user:
        password: ncdhz-multifile-sub-password
    app:
        name: multifile-sub-name

    config:
        path: ./multifile_sub_two.yaml
    ```

2. 配置文件二[examples/tutorial/multifile/multifile_sub_two.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/multifile/multifile_sub_two.yaml)

    ```yaml
    user:
        username: ncdhz-multifile-sub-username
    app:
        id: multifile-sub-id
    ```

3. 源码文件[examples/tutorial/multifile/multifile_sub.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/multifile/multifile_sub.py)

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
        Config.init(path.join(path.dirname(__file__), 'multifile_sub_one.yaml'), config_path='config.path')
        print(User.password)
        print(User.username)
        print(App.name)
        print(App.id)
    ```

## 获取配置

> 配置分为映射配置`get_config`和所有配置`get_all_config`，其中`get_config`表示通过`init`或者`refresh`函数映射的配置，`get_all_config`表示获取含有`@Config`修饰器的所有配置。

+ 配置文件[examples/tutorial/config/config.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/config/config.yaml)

    ```yaml
    User:
        username: username
    ```

+ 源码文件[examples/tutorial/config/config.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/config/config.py)

    ```python
    from no_config import Config
    from os import path

    @Config()
    class User:
        password = 'password'
        username = None

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'config.yaml'))
        # 获取映射配置
        print(Config.get_config())
        # 获取所有配置
        print(Config.get_all_config())
    ```

## 刷新配置

> 直接刷新配置不会合并，而会替换所有配置。使用参数`merge=True`可以保存已经存在的配置，并对配置进行刷新。

1. 配置文件[examples/tutorial/refresh/refresh.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/refresh/refresh.yaml)

    ```yaml
    User:
        username: username
    ```

2. 源码文件[examples/tutorial/refresh/refresh.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/refresh/refresh.py)

    ```python
    from no_config import Config
    from os import path

    @Config()
    class User:
        password = None
        username = None

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'refresh.yaml'))
        print(Config.get_config())
        Config.refresh({
            'user': {
                'password': 'password'
            }
        })
        print(Config.get_config())
    ```

3. 覆盖配置[examples/tutorial/refresh/refresh_cover.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/refresh/refresh_cover.py)

    ```python
    from no_config import Config
    from os import path

    @Config()
    class User:
        password = None
        username = None

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'refresh.yaml'))
        print(Config.get_config())
        Config.refresh({
            'user': {
                'password': 'password'
            }
        }, cover=True)
        print(Config.get_config())
    ```

## 保存配置

> 保存配置使用的是`get_all_config`，所以可以保存所有配置。

1. 配置文件[examples/tutorial/save/save.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/save/save.yaml)

    ```yaml
    User:
        username: username
    ```

2. 源码文件[examples/tutorial/save/save.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/save/save.py)

    ```python
    from no_config import Config
    from os import path

    class Password:
        def __init__(self):
            self.password = 'password'

    @Config(type=dict(password=Password))
    class User:
        password = Password()
        username = None

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'save.yaml'))
        # 默认格式yaml，文件名为uuid1
        Config.save()
        # 指定文件名
        Config.save(file_path='config.yaml')
        # 指定文件名和文件类型
        Config.save(file_path='config.json', file_type='json')
        Config.save(file_path='config.toml', file_type='toml')
    ```
