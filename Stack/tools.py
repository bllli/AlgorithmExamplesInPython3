"""工具函数"""
import functools


def log(fun):
    """记录某函数的调用及返回值"""
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        return_value = fun(*args, **kwargs)
        print('%-5s %r' % (fun.__name__, return_value))  # 注释此行取消log
        return return_value
    return wrapper
