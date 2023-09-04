class Config:

    __config_data = {}
    __config_class = {}
    __is_init = False
    __class = '__class'

    def __init__(self, name=None, type=None):
        self.__name = name
        self.__type = type

    def __new__(cls, *args, **kwargs):
        if len(args):
            return Config.__decorate(args[0])
        return super().__new__(cls)

    @staticmethod
    def __init(config_data, config_class):

        if type(config_class) is tuple:
            if type(config_data) is dict:
                Config.__input(config_data, config_class[0], config_class[1])
            return

        for class_key in config_class:
            if class_key == Config.__class:
                Config.__init(config_data, config_class[class_key])
            else:
                if class_key in config_data and type(config_data[class_key]) == dict:
                    Config.__init(config_data[class_key],
                                  config_class[class_key])

    @staticmethod
    def __input(config, clazz, type_):
        if type(config) != dict:
            raise ValueError(
                f'[class: {clazz}] [config: {config}] config error.')
        for key in config:
            if key in clazz.__dict__:
                value = clazz.__dict__[key]
                if type(value) not in set([list, str, int, dict, float]) and value is not None and key not in type_:
                    try:
                        Config.__input(config[key], value, {})
                    except:
                        raise ValueError(
                            f'[class: {clazz}] [config: {config}] [key: {key}] config error.')
                else:
                    data = config[key]
                    if key in type_:
                        config_value = config[key]
                        if type(config_value) is list:
                            data = [Config.__init_obj(
                                type_[key], cv) for cv in config_value]
                        else:
                            data = Config.__init_obj(type_[key], config[key])
                    exec(f'clazz.{key}=data')

    @staticmethod
    def __init_obj(obj, paras):
        ps = {}
        no_ps = {}
        try:
            co_varnames = obj.__init__.__code__.co_varnames
            for key in paras:
                if key in co_varnames:
                    ps[key] = paras[key]
                else:
                    no_ps[key] = paras[key]
        except:
            no_ps = paras

        new_ = obj(**ps)

        for key in no_ps:
            exec(f'new_.{key}=no_ps[key]')

        return new_

    @staticmethod
    def __init_class(names, clazz, type_):
        config = Config.__config_data
        for name in names:
            config = config.get(name)
            if config is None:
                return
        Config.__input(config, clazz, type_)

    def __call__(self, clazz):
        return Config.__decorate(clazz, self.__name, self.__type)

    @staticmethod
    def __decorate(clazz, name=None, type=None):
        if name is None:
            name = clazz.__name__.lower()

        names = name.split('.')

        config_class = Config.__config_class
        for name in names:
            config_class = config_class.setdefault(name, {})

        type_ = type if type else {}
        config_class[Config.__class] = (clazz, type_)

        if Config.__is_init:
            Config.__init_class(names, clazz, type_)

        return clazz

    @staticmethod
    def init(file_path, file_type='yaml'):
        with open(file_path, 'r', encoding='utf-8') as f:
            if file_type == 'yaml':
                import yaml
                Config.__config_data = yaml.load(f, Loader=yaml.FullLoader)
            elif file_type == 'json':
                import json
                Config.__config_data = json.load(f)
            
        Config.__is_init = True
        Config.__init(Config.__config_data, Config.__config_class)
