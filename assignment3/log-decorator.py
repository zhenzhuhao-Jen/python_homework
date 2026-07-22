#Task 1

import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        if len(args) > 0:
            args_list = list(args)
        else:
            args_list = "none"
        
        if len(kwargs) > 0:
            kwargs_list = kwargs
        else:
            kwargs_list = "none"
        function_value = func(*args, **kwargs)   
        log_info = f" function: {func.__name__}\n positonal parameters: {args_list}\n keyword parameters: {kwargs_list}\n return: {function_value}"
        logger.log(logging.INFO, log_info)
    return wrapper


@logger_decorator

def greet():
    print("Hello, World!")
@logger_decorator
def boolean(*args):
    return True
@logger_decorator
def yyui(*kwargs):
    return logger_decorator

greet()
boolean("hush")
yyui()
