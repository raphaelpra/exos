# dumped from a live coding on nbhosting

class Atom:
    def __init__(self, value):
        self.value = value
    def eval(self):
        return self.value

class Integer(Atom):
    pass
class Float(Atom):
    pass



class Negative:
    def __init__(self, *args):
        if len(args) != 1:
            raise TypeError("wrong number of args")
        self.x = args[0]
    def eval(self):
        return - self.x.eval()


class N_ary:
    # requires attributes
    # neutral : element neutre
    # binary: une fonction (x, y) -> z
    def __init__(self, *children):
        if len(children) < 2:
            raise TypeError(f"wrong args {children}")
        self.children = children

    def eval(self):
        result = self.neutral
        for child in self.children:
#            print(f"combining {result} and {child}")
            result = self.binary(result, child.eval())
        return result

class Plus(N_ary):
    neutral = 0
    @staticmethod
    def binary(x, y):
        return x + y


class Multiply(N_ary):
    neutral = 1
    @staticmethod
    def binary(x, y):
        return x * y

class Binary:
    # requires a binary function
    def __init__(self, *children):
        if len(children) != 2:
            raise TypeError(f"wrong args {children}")
        self.lhs, self.rhs = children
    def eval(self):
        return self.binary(self.lhs.eval(), self.rhs.eval())
    
class Minus(Binary):
    binary = lambda self, x, y: x - y

class Divide(Binary):
    binary = lambda self, x, y: x / y

