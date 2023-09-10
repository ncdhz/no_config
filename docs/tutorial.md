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
        Config.init(path.join(path.dirname(__file__), 'multiple_target.yaml'))
        print(User.password)
        print(User.username)
        print(App.name)
        print(App.id)
    ```

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

## 实体注入

> 当某个字段是一个实体时，可以通过让字段等于实体的方式注入配置。通过此方式注入的属性都是静态的。

1. 配置文件[examples/tutorial/class_inject/class_inject.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/class_inject/class_inject.yaml)

    ```yaml
    app:
        name: class-inject-name
        user:
            username: ncdhz-class-inject
    ```

2. 源码文件[examples/tutorial/class_inject/class_inject.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/class_inject/class_inject.py)

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
        Config.init(path.join(path.dirname(__file__), 'class_inject.yaml'))
        print(App.name)
        print(App.user.username)
        print(User.username)
    ```

## 类别注入

> 通过`Config`中的`type`参数可以配置类中某静态属性属于那个实体，其中实体的注入使用的初始化函数。如3注入处理在`username`中添加了`_xxx`字符串（初始化函数参数名应和配置文件一致）。

1. 配置文件[examples/tutorial/type_inject/type_inject.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/type_inject/type_inject.yaml)

    ```python
    app:
        name: type-inject-name
        user:
            username: ncdhz-type-inject
    ```

2. 源码文件[examples/tutorial/type_inject/type_inject.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/type_inject/type_inject.py)

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
        Config.init(path.join(path.dirname(__file__), 'type_inject.yaml'))
        print(App.name)
        print(App.user.username)
        print(User.username)
    ```

3. 注入处理[examples/tutorial/type_inject/type_inject_handle.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/type_inject/type_inject_handle.py)

    > 类别注入中可以通过初始化函数对注入的配置进行处理。

    ```python
    from no_config import Config
    from os import path

    class User:
        def __init__(self, username):
            username += '_xxx'
            self.username = username

    @Config(type=dict(user=User))
    class App:
        name = None
        user = None

    if __name__ == '__main__':
        Config.init(path.join(path.dirname(__file__), 'type_inject.yaml'))
        print(App.name)
        print(App.user.username)
    ```

4. 注入方法

    > 如果你想对某个属性进行处理，那么你可以在`type`中给它指定一个处理函数。

    + 配置文件[examples/tutorial/type_inject/type_inject_func.yaml](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/type_inject/type_inject_func.yaml)

        ```yaml
        app:
            name: type-inject-name
        ```
    
    + 源码文件[examples/tutorial/type_inject/type_inject_func.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/type_inject/type_inject_func.py)
    
        ```python
        from no_config import Config
        from os import path

        def split_name(name):
            return name.split('-')

        @Config(type=dict(name=split_name))
        class App:
            name = None

        if __name__ == '__main__':
            Config.init(path.join(path.dirname(__file__), 'type_inject_func.yaml'))
            print(App.name)
        ```



## 多个文件

> 实际生产中配置可能会跨配置文件（可以分为常改配置和非常改配置），下面演示了两种不同配置文件的整合配置。

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
                    (path.join(current_dir, 'multifile_two.json'), 'json')])
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

> 直接刷新配置不会合并，而会替换所有配置。使用参数`merge=True`可以保存已经映射的配置。

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

3. 合并配置[examples/tutorial/refresh/refresh_merge.py](https://github.com/ncdhz/no_config/blob/main/examples/tutorial/refresh/refresh_merge.py)

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
        }, merge=True)
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
