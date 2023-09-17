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
Config.init(file_path, file_type='yaml', merge=False)
```

+ `file_path` 文件路径，字符串或者数组。
    + 当为字符串时就代表文件路径。
    + 当为数组时每一个元素可以是文件路径也可以是数组，是数组则第一个元素表示文件路径第二个元素表示文件类型，其中的文件类型优先于`file_type`参数。

        ```python
        ['file_path', ['file_path', 'file_type'], 'file_path']
        ```

+ `file_type` 文件类型，当文件路径中没有指定类型时使用。可选参数`yaml`、`json`和`toml`。

+ `merge` 是否合并新和原有配置。

## 刷新

```python
Config.refresh(config_data=None, merge=False)
```

+ `config_data` 配置数据，字典格式，可以读取配置文件通过此函数刷新配置。

+ `merge` 是否合并新和原有配置。

## 获取配置

```python
Config.get_config()
```

> 获取映射的配置文件。

## 获取所有配置

```python
Config.get_all_config()
```

> 获取所有配置文件。

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

> 这是一个注入修饰器，详细信息见[@Inject](./inject_tutorial.md) 
