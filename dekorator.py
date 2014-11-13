from functools import wraps


def mydecorator(f):

    @wraps(f)
    def wrapped(*args, **kwargs):
        print ("Before decorated function")
        r = f(*args, **kwargs)
        print ("After decorated function")
        return r

    return wrapped


@mydecorator
def myfunc(myarg):
    print ("my function", myarg)
    return "return value"


r = myfunc('asdf')
print (r)
# Before decorated function
# my function asdf
# After decorated function
# return value


def set_namespace(ns):

    def dekorator(f):

        @wraps(f)
        def wrapped(*args, **kwargs):
            print(ns)
            print ("Before decorated function")
            r = f(*args, **kwargs)
            print ("After decorated function")
            return r

        return wrapped
    return dekorator


@set_namespace('abc')
def funkcja(myarg):
    print ("my function", myarg)
    return "return value"


r = funkcja('asdf')
print (r)
# Before decorated function
# my function asdf
# After decorated function
# return value
