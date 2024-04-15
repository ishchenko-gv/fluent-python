import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __boolean__(self):
        return bool(abs(self))

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(4, 7)
v2 = Vector(5, 3)

print('add', v1 + v2)
print('abs', abs(v1))
print('multiply', v1 * 4)
