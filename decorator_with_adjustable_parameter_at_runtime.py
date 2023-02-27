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

        def set_weight(value):
            nonlocal weight
            weight = value

        def set_to_print(boolean):
            nonlocal to_print
            to_print = boolean

        methods = [set_weight, set_to_print]
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

