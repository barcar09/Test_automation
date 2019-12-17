import time


def decorator_underline(hello):
    def make_underline():

        text = "<b>"+hello()+"</b>"
        return text

    return make_underline


def delay_decorator(delay):
    def decorated_function(to_decorate):
        def arg_to_function(*arg):
            time.sleep(delay)
            to_decorate(*arg)
        return arg_to_function
    return decorated_function


@decorator_underline
def hello():
    return "hello world"


@delay_decorator(delay=10)
def name_print(my_name):
    print("my name is {}".format(my_name))


print(hello())
name_print("Bartek")