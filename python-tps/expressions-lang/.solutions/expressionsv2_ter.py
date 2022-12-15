# votre code

class Atom:
    def __init__(self, value):
        self.value = value
    def eval(self, env):
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
    def eval(self, env):
        return - self.x.eval(env)


class N_ary:
    # requires attributes
    # neutral : element neutre
    # binary: une fonction (x, y) -> z
    # checker: une fonction sur le nombre d'arguments
    # par ex:   is_binary(2) -> True is_binary(_) -> False
    def __init__(self, *children):
        if not self.checker(len(children)):
            raise TypeError(f"wrong args {len(children)} with {self}")
        self.children = children

    def __repr__(self):
        return f"<{self.__class__.__name__} ...>"

    def eval(self, env):
        first, second, *others = self.children
        result = self.binary(first.eval(env), second.eval(env))
        for child in others:
#            print(f"combining {result} and {child}")
            result = self.binary(result, child.eval(env))
        return result

class Plus(N_ary):
    @staticmethod
    def checker(nb_args):
        return nb_args >= 2
    @staticmethod
    def binary(x, y):
        return x + y


class Multiply(N_ary):
    @staticmethod
    def checker(nb_args):
        return nb_args >= 2
    @staticmethod
    def binary(x, y):
        return x * y

class Minus(N_ary):
    @staticmethod
    def checker(nb_args):
        return nb_args == 2
    binary = lambda self, x, y: x - y

class Divide(N_ary):
    @staticmethod
    def checker(nb_args):
        return nb_args == 2
    binary = lambda self, x, y: x / y


###
class Variable:
    def __init__(self, name):
        self.name = name
    def eval(self, env):
        return env[self.name]

class Expressions:
    def __init__(self, *children):
        if len(children) == 0:
            raise TypeError(f"wong number of args in Expressions")
        self.children = children
    def eval(self, env):
        for child in self.children:
            result = child.eval(env)
        return result

class Assignment:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
    def eval(self, env):
        result = self.expr.eval(env)
        env[self.name] = result
        return result