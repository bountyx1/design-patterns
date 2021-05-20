def logger(func):
    def wrapper(*args,**kwargs):
        print(f"Exec fn: {func.__name__} \nArguments **kwargs: {kwargs} \n*args: {args} ")
        output = func(*args,**kwargs)
        print(f"Result of {func.__name__}: {output}")
        return output
    return wrapper



@logger
def hello(**kwargs):
    return kwargs['name']


print(hello(name="nabi",age=22))
