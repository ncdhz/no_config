import types
import inspect
from .inject import Inject

class Config:

    __config_data = {}
    __config_class = {}
    __is_init = False
    __class = '__class'

    def __init__(self, name:str=None, type:dict=None):
        '''
        name: Specify the configuration class mapping name. Multiple levels can be segmented using `.`.
            ```
            @Config(name='app.user')
            class User:
                password = None
                username = None
            ```
            
        type: What type of property is specified. 
            ```
            class User:
                username = None

            @Config(type=dict(user=User))
            class App:
                name = None
                user = None
            ```
        '''
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
                try:
                    vars(value)
                    try:
                        if type(value) in {types.FunctionType, types.MethodType, Inject}:
                            data = Config.__init_obj(value, config[key])
                            exec(f'clazz.{key}=data')
                        else:
                            Config.__input(config[key], value, {})
                    except:
                        raise ValueError(
                            f'[class: {clazz}] [config: {config}] [key: {key}] config error.')
                except TypeError:
                    data = config[key]
                    if key in type_:
                        if type(data) is list:
                            data = [Config.__init_obj(
                                type_[key], cv) for cv in data]
                        else:
                            data = Config.__init_obj(type_[key], data)
                    exec(f'clazz.{key}=data')

    @staticmethod
    def __init_obj(obj, paras):
        
        if type(paras) is not dict:
            return obj(paras)
        
        ps = {}
        if type(obj) == Inject:
            args = obj.args
        else:
            args = inspect.getfullargspec(obj).args
        
        for key in paras:
            if key in args:
                ps[key] = paras[key]

        new_ = obj(**ps)

        try:
            dict_ = vars(new_)
            for key in paras:
                if key not in dict_:
                    exec(f'new_.{key}=paras[key]')
        except:
            pass

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
    def __name_format(name):
        ns = name[0]
        for n in name[1:]:
            if 'A' <= n <= 'Z':
                ns += f'_{n}'
            else:
                ns += n
        return ns.lower()

    @staticmethod
    def __decorate(clazz, name=None, type=None):
        if name is None:
            name = clazz.__name__

        names = name.split('.')
        
        names[0] = Config.__name_format(names[0])

        config_class = Config.__config_class
        for name in names:
            config_class = config_class.setdefault(name, {})

        type_ = type if type else {}
        config_class[Config.__class] = (clazz, type_)

        if Config.__is_init:
            Config.__init_class(names, clazz, type_)

        return clazz

    @staticmethod
    def __read_config(file_path, file_type):
        with open(file_path, 'r', encoding='utf-8') as f:
            if file_type == 'yaml':
                import yaml
                config = yaml.load(f, Loader=yaml.FullLoader)
            elif file_type == 'json':
                import json
                config = json.load(f)
            elif file_type == 'toml':
                import toml
                config = toml.load(file_path)
            else:
                raise TypeError(f'File type not supported. [{file_type}]')
        return config if config else {}
    
    @staticmethod
    def __merge_dict(obj, obj1, refresh=False):
        obj_type = type(obj)
        obj1_type = type(obj1)

        if obj_type == list and obj1_type == list:
            obj.extend(obj1)
        elif obj_type == set and obj1_type == set:
            obj.update(obj1)
        elif obj_type == dict and obj1_type == dict:
            for key in obj1:
                if key in obj:
                    obj[key] = Config.__merge_dict(obj[key], obj1[key])
                else:
                    obj[key] = obj1[key]
        else:
            if refresh:
                return obj1
            raise ValueError('Duplicate configuration attributes.')
        return obj
        
    @staticmethod
    def init(file_path, file_type='yaml', merge=False):
        '''
        file_path: The file path can be a string or an array.
            array: [file_path, file_path, [file_path, file_type]]
            The elements in the array can be strings or arrays.
            When it is an array, the first element should be the file path, and the second element should be the file type.
        file_type: Used when the file path is a string or a string in an array.
            yaml | json | toml
        merge: Merge new and existing configurations.
        '''
        if type(file_path) == str:
            config_data = Config.__read_config(file_path, file_type)
        elif type(file_path) == list or type(file_path) == tuple:
            config_data = {}
            for fp in file_path:
                if type(fp) == str:
                    cd = Config.__read_config(fp, file_type)
                else:
                    if len(fp) == 1:
                        cd = Config.__read_config(fp[0], file_type)
                    else:
                        cd = Config.__read_config(fp[0], fp[1])
                config_data = Config.__merge_dict(config_data, cd)
        
        for key in list(config_data.keys()):
            value = config_data.pop(key)
            config_data[Config.__name_format(key)] = value

        Config.refresh(config_data, merge)

    @staticmethod
    def refresh(config_data=None, merge=False):
        '''
        config_data: Configuration data is in a dictionary format.
        merge: Merge new and existing configurations.
        '''
        if config_data is not None:
            if merge:
                Config.__config_data = Config.__merge_dict(Config.__config_data, config_data, True)
            else:
                Config.__config_data = config_data

        Config.__is_init = True
        if merge:
            if config_data is None:
                raise TypeError('[merge] is True, [config_data] cannot be empty')
            Config.__init(config_data, Config.__config_class)
        else:
            Config.__init(Config.__config_data, Config.__config_class)

    @staticmethod
    def get_config():
        '''
        return: Read configuration file.
        '''
        return Config.__config_data

    @staticmethod
    def get_all_config():
        '''
        return: All configuration files.
        '''
        def __get_all_config(data, is_clazz):
            result = {}
            if is_clazz:
                params = vars(data)
                for k in params:
                    if not k.startswith('__') and not k.endswith('__') and type(params[k]) not in {types.FunctionType, staticmethod}:
                        try:
                            vars(params[k])
                            result[k] = __get_all_config(params[k], True)
                        except:
                            result[k] = params[k]
            else:
                for key in data:
                    if key == Config.__class:
                        result.update(__get_all_config(data[key][0], True))
                    else:
                        result[key] = __get_all_config(data[key], False)
            return result

        return __get_all_config(Config.__config_class, False)

    @staticmethod
    def save(file_path=None, file_type='yaml', **kwargs):
        '''
        file_path: Specify the save path, default to uuid.
        file_type: File type, default to yaml.
            yaml | json | toml
        kwargs: Other saved parameters.
        '''
        if file_path is None:
            from uuid import uuid1
            file_path = f'{uuid1()}.{file_type}'
        
        if file_type not in {'yaml', 'json', 'toml'}:
            raise TypeError(f'File type not supported. [{file_type}]')
        
        data = Config.get_all_config()
        with open(file_path, 'w', encoding='utf-8') as f:
            if file_type == 'yaml':
                import yaml
                yaml.dump(data, f, **kwargs)
            elif file_type == 'json':
                import json
                json.dump(data, f, **kwargs)
            else:
                import toml
                toml.dump(data, f, **kwargs)

    @staticmethod
    def inject(obj=None, **kwargs):
        return Inject(obj=obj, **kwargs)
