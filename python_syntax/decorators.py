from functools import wraps,partial

def outer_fn(msg):
    message=msg

    def inner_fn():
        print(message)
    
    return inner_fn

hi_func=outer_fn('Hi')
bye_func=outer_fn('goodbye')

def decorator(fn):
    def wrapper_function(*args,**kwargs):
        return fn(*args,**kwargs)
    
    return wrapper_function

@decorator
def display_fn():
    print('display something!')

@decorator
def display_info(name,age):
    r='He is {} and {}-year-old '.format(name,age)
    print(r)

# display_info('Tom',23)
# display_fn=decorator(display_fn)
# display_fn()


def my_logger(origin_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(origin_func.__name__),level=logging.INFO)
    @wraps(origin_func)
    def wrapper(*args,**kwargs):
        logging.info(
            'ran with args:{} and  kwargs {}'.format(*args)
        )
        return origin_func(*args,**kwargs)
    return wrapper

def my_timer(origin_func):
    import time
    @wraps(origin_func)
    def wrapper(*args,**kwargs):
        t1=time.time()
        result=origin_func(*args,**kwargs)

        t2=time.time()-t1
        print('{} ran in {} sec'.format(origin_func.__name__,t2))

        return result

    return wrapper
import time
@my_logger
@my_timer
def display_info(name,age):
    time.sleep(2)
    r='He is {} and {}-year-old '.format(name,age)
    print(r)

display_info('Weifo',23)