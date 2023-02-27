"""
    This program demonstrates two aspects:
    1. Set decorator's parameters in runtime.
    2. Accept decorator call with or without parentheses.

    Remember, decorator should always be a callable to accept decorated
    function as its first parameter. Returning a 'partial' of itself 
    can always have the decorator ready to accept decorated function.
"""


from functools import partial, wraps


def weighted(func=None, weight=1, is_show=True):
    if func is None:
        return partial(weighted, weight=weight, is_show=is_show)

    @wraps(func)
    def inner(*args, **kwargs):
        nonweighted_result = func(*args, **kwargs)
        weighted_result =nonweighted_result * weight
        if is_show:
            print(f'Non-weighted result: {nonweighted_result}')
            print(f'Weighted result: {weighted_result}, weight: {weight}')
        return weighted_result

    def set_weight(value):
        nonlocal weight
        weight = value

    def set_is_show(boolean):
        nonlocal is_show
        is_show = boolean

    methods = (m for m in locals().values() if m != inner and
                                             isinstance(m, type(inner)))
    for method in methods:
        setattr(inner, method.__name__, method)

    return inner


@weighted
#@weighted(weight=10)
#@weighted(weight=10, is_show=False)
def add(x, y):
    return x + y


a = add
print(f'(default weight, default is_show): {a(2, 3)}')
a.set_weight(2)
print(f'(set weight to 2, default is_show): {a(2, 3)}')
a.set_is_show(False)
print(f'(set weight to 2, set is_show False): {a(2, 3)}')
a.set_is_show(True)
print(f'(set weight to 2, set is_show True): {a(2, 3)}')
