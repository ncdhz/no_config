import yaml
import json

class Config:

    __config_data = {}
    __config_class = {}
    __is_init = False
    __class = '__class'

    def __init__(self, name=None):
        self.__name = name

    def __new__(cls, *args, **kwargs):
        if len(args):
            return Config.__decorate(args[0])
        return super().__new__(cls)

    @staticmethod
    def __init(config_data, config_class):

        if type(config_class) is not dict:
            if type(config_data) is dict:
                Config.__input(config_data, config_class)
            return

        for class_key in config_class:
            if class_key == Config.__class:
                Config.__init(config_data, config_class[class_key])
            else:
                if class_key in config_data and type(config_data[class_key]) == dict:
                    Config.__init(config_data[class_key],
                                  config_class[class_key])

    @staticmethod
    def __input(config, clazz):
        if type(config) != dict:
            raise ValueError(f'[class: {clazz}] [config: {config}] config error.')
        for key in config:
            if key in clazz.__dict__:
                value = clazz.__dict__[key]
                if type(value) == type:
                    try:
                        Config.__input(config[key], value)
                    except:
                        raise ValueError(f'[class: {clazz}] [config: {config}] [key: {key}] config error.')
                else:
                    exec(f'clazz.{key}={json.dumps(config[key])}')

    @staticmethod
    def __init_class(names, clazz):
        config = Config.__config_data
        for name in names:
            config = config.get(name)
            if config is None:
                return
        Config.__input(config, clazz)

    def __call__(self, clazz):
        return Config.__decorate(clazz, self.__name)

    @staticmethod
    def __decorate(clazz, name=None):
        if name is None:
            name = clazz.__name__

        names = name.split('.')

        config_class = Config.__config_class
        for name in names:
            config_class = config_class.setdefault(name, {})

        config_class[Config.__class] = clazz

        if Config.__is_init:
            Config.__init_class(names, clazz)

        return clazz

    @staticmethod
    def init(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            Config.__config_data = yaml.load(f, Loader=yaml.FullLoader)
        Config.__is_init = True
        Config.__init(Config.__config_data, Config.__config_class)
