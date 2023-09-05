# no_config

把`yaml`、`json`和`toml`等配置文件映射为类，需要很多`冗余代码`或者`魔术字符串`。这对代码的维护工作提出了更高的要求，[no_config](https://github.com/ncdhz/no_config)能简化这种映射，仅仅需要两行代码即可完成映射。更多文档信息请参考[https://ncdhz.github.io/no_config](https://ncdhz.github.io/no_config)。

## 快速开始

下面将用一个简短的例子介绍本库该怎么使用，例子中使用的源码在[examples/start/start.py](https://github.com/ncdhz/no_config/blob/main/examples/start/start.py)。

1. 配置文件

    ```yaml
    # 创建配置文件start.yaml
    user:
        username: ncdhz
        password: ncdhz
    ```

2. 源码文件

    ```python
    from os import path
    from no_config import Config
    
    # 配置注入
    @Config
    class User:
        password = None
        username = None

    if __name__ == '__main__':
        # 配置初始化
        # 全局只需一次初始化
        # 在更改配置之后可以通过此函数刷新配置
        Config.init(path.join(path.dirname(__file__), 'start.yaml'))
        print(User.password)
        print(User.username)
    ```

## 安装

### pip安装

```bash
pip install no_config
```

### 源码安装

```bash
git clone https://github.com/ncdhz/no_config.git
# 进入no_config目录执行下面语句
pip install .
```
