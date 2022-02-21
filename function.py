def get_reverse(*args):
    return args[::-1]


def decorator(func):
    def wrapper(*args, **kwargs):
        return f"<html>{func(*args, **kwargs)}</html>"
    return wrapper


@decorator
def some_text(*args, **kwargs):
    return "Hello"


# print(get_reverse(1, 2, 3, 8, -2))
# print(some_text())
