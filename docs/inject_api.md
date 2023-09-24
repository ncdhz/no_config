## @Inject

```python
@Inject(config_inject:str=None, type:dict=None)
```
> 类中注入某个属性可以通过此修饰器，只需要在类上添加此修饰器就能完成属性自动注入。

+ `type`: 需要指定注入参数为某类，或者需要对注入参数进行处理时可以使用。具体例子见[类注入](./inject_tutorial?id=类注入)或[方法注入](./inject_tutorial?id=方法注入)。

+ `config_inject`: 需要配置注入的别名，默认为`config_inject`，见[配置注入](./inject_tutorial?id=配置注入)和[配置注入别名](./inject_tutorial?id=配置注入别名)