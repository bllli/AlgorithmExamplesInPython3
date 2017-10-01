import functools


def log(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        return_value = fun(*args, **kwargs)
        print('%-5s %r' % (fun.__name__, return_value))  # 注释此行取消log
        return return_value
    return wrapper
