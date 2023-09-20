import inspect


class Inject:
    '''
    Use:
        from no_config import Inject

        @Inject
        class User:
            def __init__(name):
                pass
        
        if __name__ == '__main__':
            user = User('ncdhz')  
            print(user.name)
    '''
    def __init__(self, obj=None, config_inject:str=None, type:dict=None):
        self.__obj = obj
        self.__type = type
        self.__config_inject = config_inject if config_inject else 'config_inject'
        self.__fullargspec()

    def __fullargspec(self):
         if self.__obj is not None:
            self.args_defaults = {}
            self.args = []
            for name, param in inspect.signature(self.__obj).parameters.items():
                self.args.append(name)
                if param.default is not inspect._empty:
                    self.args_defaults[name] = param.default

    def __handle(self, *args, **kwargs):

        for i, arg in enumerate(args):
            kwargs[self.args[i]] = arg
        
        for key in self.args_defaults:
            if key not in kwargs:
                kwargs[key] = self.args_defaults[key]
        
        if self.__config_inject in kwargs:
            config = kwargs[self.__config_inject]
            kwargs.pop(self.__config_inject)
            for key in config:
                kwargs[key] = config[key]

        if self.__type and type(self.__type) == dict:
            for key in kwargs:
                value = kwargs[key]
                __value = self.__type.get(key)
                if __value:
                    if type(value) is dict:
                        kwargs[key] = __value(**value)
                    elif type(__value) is list and len(__value) > 0:
                        kwargs[key] = [__value[0](**v) if type(v) is dict else __value[0](v) for v in value]
                    else:
                        kwargs[key] = __value(value)

        o = self.__obj(**kwargs)
        try:
            dict_ = vars(o)

            for key in kwargs:
                if key not in dict_:
                    exec(f'o.{key}=kwargs[key]')
        except:
            pass

        return o

    def __call__(self, *args, **kwargs):
        if self.__obj is None:
            self.__obj = args[0]
            self.__fullargspec()
            return self.__handle
        return self.__handle(*args, **kwargs)

        

