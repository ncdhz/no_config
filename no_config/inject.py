import inspect
import types


class Inject:

    def __init__(self, obj=None, **kwargs):
        self.__obj = obj
        self.__kwargs = kwargs
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

        for key in kwargs:
            value = kwargs[key]
            __value = self.__kwargs.get(key)
            if __value:
                if type(value) is dict:
                    kwargs[key] = __value(**value)
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

        

