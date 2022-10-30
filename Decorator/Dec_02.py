import math

def pretty_namber(function):
    def new_function(*args, **kwargs):
        number = function(*args, **kwargs)
        return '{:.2f}'.format(number)

    return new_function

@pretty_namber
def circle_area(radius):
    return math.pi * (radius ** 2)

@pretty_namber
def ellipse_area(width, height):
    return math.pi / 4 * width * height

print(circle_area(5))
print(ellipse_area(10, 5))