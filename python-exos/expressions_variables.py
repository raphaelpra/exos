class Plus:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __str__(self):
        return f"Plus [{self.left} + {self.right}]"
    def eval(self, env=None):
        return self.right.eval(env) + self.left.eval(env)

class Mult:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __str__(self):
        return f"Mult [{self.left} * {self.right}]"
    def eval(self, env=None):
        return self.right.eval(env) * self.left.eval(env)

class Power:
    def __init__(self, what, power):
        self.what = what
        self.power = power
    def __str__(self):
        return f"Power [{self.what} ** {self.power}]"
    def eval(self, env=None):
        return self.what.eval(env) ** self.power.eval(env)

class Number:
    def __init__(self, atom):
        self.atom = atom
    def __str__(self):
        return f"[N {self.atom}]"
    def eval(self, env=None):
        return self.atom

class Variable:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"[V {self.name}]"
    # pour faire simple
    # quand la variable n'est pas définie
    # on retourne 0
    def eval(self, env=None):
        env = env or {}
        return env.get(self.name, 0)

# Ou aissu bien d'ailleurs
# NameSpace = dict
class NameSpace(dict): pass

if __name__ == '__main__':
    # compat
    exps = [
        Mult(Number(27), Plus(Number(43), Number(12))),
        Power(Mult(Number(1), Number(3)),
              Plus(Number(1), Number(2)))
        ]
    for exp in exps:
        print(f"exp = {exp} -> eval = {exp.eval()}")

    # with envs
    exp = Mult(Variable('x'), Variable('y'))
    envs = [
        NameSpace(x=12, y=10),
        NameSpace(x=12, z=10),
        ]
    line = 10*'=' + "\n"
    space = 3*' '
    for env in envs:
        eval = exp.eval(env)
        print(f"{line}{space}exp = {exp}\n{space}env = {env}\n{space}eval = {eval}")
