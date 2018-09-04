
def list_unfolder(f):
    """Decorator to use a list or tuple instead of several arguments in a function call"""
    def wrapper(*args):
        if len(args) == 1 \
           and (isinstance(args[0], list) or isinstance(args[0], tuple)):
            return f(*args[0])
        elif len(args) == 3:
            return f(*args)
        raise Exception("Method '%s' can be called with three numbers or a list of three numbers" % f.__name__)
    return wrapper

