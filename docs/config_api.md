## @Config

```python
@Config(name=None, type=None)
```

+ `name` 明确映射路径，多等级使用`.`分割，如`app.user`。

    ```python
    @Config(name='app.user')
    class User:
        password = None
        username = None
    ```

+ `type` 属性的映射类型。

    ```python
    class User:
        def __init__(self, username):
            self.username = username

    @Config(type=dict(user=User))
    class App:
        name = None
        user = None
    ```

## 初始化

```python
Config.init(file_path, file_type='yaml', config_path=None, cover=False)
```

+ `file_path` 文件路径，字符串或者数组。
    + 当为字符串时就代表文件路径。
    + 当为字典时格式如下，其中`path`表示配置文件本地路径，`url`表示配置文件远程路径，`type`表示配置文件类型`yaml`、`json`和`toml`三选一。
        
        ```python
        {
            'path': str | None,
            'url': str | None,
            'type': str | None
        }
        ```

    + 当为数组时每一个元素可以是字符串或者字典，为字符串表示本地文件路径，为字典格式与上述相同。

        ```python
        ['file_path', {'path': str | None, 'url': str | None, 'type': str | None}, 'file_path']
        ```

+ `file_type` 文件类型，当文件路径中没有指定类型时使用。可选参数`yaml`、`json`和`toml`。

+ `cover` 是否覆盖原有配置。

## 刷新配置

```python
Config.refresh(config_data=None, cover=False)
```

> 对部分配置进行更改时使用，详细信息见[刷新配置](./function_tutorial?id=刷新配置)。

+ `config_data` 配置数据，字典格式，可以读取配置文件通过此函数刷新配置。

+ `cover` 是否覆盖原有配置。

## 获取配置

```python
Config.get_config()
```

> 获取映射的配置文件，详细信息见[获取配置](./function_tutorial?id=获取配置)。

## 获取所有配置

```python
Config.get_all_config()
```

> 获取所有配置文件，详细信息见[获取配置](./function_tutorial?id=获取配置)。

## 保存配置

```python
Config.save(file_path=None, file_type='yaml', **kwargs)
```

+ `file_path` 保存文件的路径，默认使用`uuid1`命名。

+ `file_type` 文件类型，默认`yaml`。可选参数`yaml`、`json`和`toml`。

+ `**kwargs` 其它参数，如保存成`json`时，`json.dump`的参数。

## 参数注入

```python
@Config.inject
```

> 这是一个注入修饰器，详细信息见[@Inject](./inject_tutorial.md)。
