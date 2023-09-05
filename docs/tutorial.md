## 基础使用

通过带括号的修饰器能更好的加强编辑器的提示功能，此例子在[examples/tutorial/class/class.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/class/class.py)中。

1. 配置文件[examples/tutorial/class/class.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/class/class.yaml)

    ```yaml
    user:
        username: ncdhz
        password: ncdhz
    ```

2. 源码文件[examples/tutorial/class/class.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/class/class.py)

    ```python
    from no_config import Config
    from os import path

    @Config()
    class User:
        password = None
        username = None

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'class.yaml'))
        print(User.password)
        print(User.username)
    ```

## 文件类型

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
