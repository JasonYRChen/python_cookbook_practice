"""
    This program demonstrates setting decorator's parameters at runtime.
    The method is to build a series of setting functions with 'nonlocal'
    declaration inside, and then 'setattr' those functions to inner
    function as its attributes.
"""

from functools import wraps


def weighted_factor(weight=1, to_print=True):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            weighted_result = result * weight
            if to_print:
                print(f'Result before weighted: {result}')
                print(f'Result after weighted: {weighted_result}')
            return weighted_result

        def set_weight(value): # helper to set decorator's parameter
            nonlocal weight
            weight = value

        def set_to_print(boolean): # helper to set decorator's parameter
            nonlocal to_print
            to_print = boolean

        # setattr functions to inner
        methods = (method for method in locals().values() 
                   if method != inner and isinstance(method, type(inner)))
        for method in methods:
            setattr(inner, method.__name__, method)

        return inner
    return decorator


@weighted_factor(2, False)
def add(x, y):
    return x + y


print(add(2, 5))
add.set_weight(10)
print(add(2, 5))
add.set_to_print(True)
print(add(2, 5))
print(add.__dict__)
