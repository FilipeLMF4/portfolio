# Unlimited/unspecified positional arguments with *args
def add(*args):
    # print(args[0])
    s = 0
    for n in args:
        s += n

    return s


print(add(3, 5, 6, 10, 2, 1, 7, 50))


# Unlimited/unspecified keyword arguments with **kwargs
def calculate(n, **kwargs):
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")  # Same as kw["make"], but return None if no key present
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", seats=4)
print(my_car.model)
